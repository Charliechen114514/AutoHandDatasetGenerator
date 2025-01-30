import sys
import os
import subprocess
from pathlib import Path
python_executable_dirent    = sys.prefix

# fetch the ui-transfer executable
def fetch_uic_executable() -> str:
    pyuic_path = os.path.join(python_executable_dirent, "Scripts", "pyside6-uic.exe")
    if not os.path.exists(pyuic_path):
        print("Can not find the uic at path:{}".format(pyuic_path))
        exit(-1)
    return pyuic_path

def fetch_args_of_ui_file() -> str:
    ui_path = sys.argv[1]
    if not os.path.exists(ui_path):
        print("Can not find the ui file :(")
        exit(-1)
    return os.path.abspath(ui_path)

def fetch_args_of_possible_path_new() -> str:
    num_args = len(sys.argv) - 1
    if num_args < 2:
        return ""
    else: 
        return sys.argv[2]

def fetch_summon_ui_name(path: str):
    dirent = os.path.dirname(path)
    file_name_without_extension = Path(os.path.basename(path)).stem
    file_new_name = "ui_" + file_name_without_extension + ".py"
    return os.path.join(dirent, file_new_name)

def check_params():
    num_args = len(sys.argv) - 1
    if num_args < 1:
        print("usage: \npeotry run python {} (target_ui).ui [path_to_save]\nwith [] is optional".format(os.path.abspath(__file__)))
        exit(-1)



"""
    this file is using as the following
"""
check_params()
possible_summon_place = fetch_args_of_possible_path_new()
if possible_summon_place == "":
    uic = fetch_uic_executable()
    ui_file = fetch_args_of_ui_file()
    subprocess.run([uic, ui_file, "-o", fetch_summon_ui_name(ui_file)])





