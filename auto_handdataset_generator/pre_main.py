from Core.Common.path_utils import PathUtils
from tools.download import download
from loguru import logger

accept_non_ssl = True
model_url = "https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/latest/gesture_recognizer.task"
logger.info("starting pre-setup the project")
logger.info("pre-Building for the RC Transformations")
PathUtils.create_dirent_if_not_exsited(PathUtils.RC_PATH)
logger.info("pre-Building for the RC Transformations done")

if not PathUtils.check_paths_if_exsit(PathUtils.MODEL_PATH):
    logger.warning("Error in checking the model file, downloading the file to target place")
    PathUtils.create_dirent_if_not_exsited(PathUtils.MODEL_DIR)
    download(model_url, PathUtils.MODEL_DIR)