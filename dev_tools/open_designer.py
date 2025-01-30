import sys
import os
import subprocess

python_executable_dirent    = sys.prefix
pyside_designer_executable  = \
    os.path.join(python_executable_dirent, "Scripts", "pyside6-designer.exe")

if os.path.exists(pyside_designer_executable):
    subprocess.call(pyside_designer_executable)
else:
    print("Error in finding path: {}, rechecking if"  
          "the target is installed".format(pyside_designer_executable))