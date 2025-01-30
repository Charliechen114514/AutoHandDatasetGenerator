import requests
import zipfile
from loguru import logger
from urllib.parse import urlparse
from tqdm import tqdm
import urllib3
import warnings
import os


def download(url, download_root) -> bool:
    try:
        logger.info(f"requesting {url}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()  
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        filename = os.path.join(download_root, filename)

        total_size_in_bytes = int(response.headers.get('content-length', 0))
        logger.info(f"file size is {total_size_in_bytes} as expected!")
        with open(filename, 'wb') as file:
            with tqdm(total=total_size_in_bytes, unit='B', unit_scale=True, desc=filename) as bar:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)  # 将数据写入文件
                        bar.update(len(chunk))  # 更新进度条
        logger.info("download success!")
        return True

    except requests.exceptions.SSLError as e:
        logger.warning(f"cautions when downloading files: {e}")
        from auto_handdataset_generator.pre_main import accept_non_ssl
        if not accept_non_ssl:
            logger.error("Non SSL is not accepted! You can modified the var by accepting SSL Error!")
            return False
        logger.info(f"shell try in downloading without SSL...")
        warnings.simplefilter('ignore', urllib3.exceptions.InsecureRequestWarning)
        response = requests.get(url, stream=True, verify=False)
        response.raise_for_status()  
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        filename = os.path.join(download_root, filename)

        total_size_in_bytes = int(response.headers.get('content-length', 0))
        logger.info(f"file size is {total_size_in_bytes} as expected!")
        with open(filename, 'wb') as file:
            with tqdm(total=total_size_in_bytes, unit='B', unit_scale=True, desc=filename) as bar:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)  # 将数据写入文件
                        bar.update(len(chunk))  # 更新进度条
        logger.info("download success!")
        return True
    except requests.exceptions.RequestException as e:
        logger.error(f"cautions when downloading files: {e}")
        return False
    except zipfile.BadZipFile as e:
        logger.error(f"error when unziping files: {e}")
        return False
    except Exception as e:
        logger.error(f"error occurs: {e}")
        return False