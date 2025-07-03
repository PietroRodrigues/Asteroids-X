from cx_Freeze import setup, Executable
import os
import sys

root = os.path.dirname(os.path.abspath(__file__))
main_script = os.path.join(root, "main.py")

all_forder = ["classPack", "Assets"]

base = None
if sys.platform == "win32":
    base = "Win32GUI"

include_files = []

for folder in all_forder:  # Aqui 'folder' é definido
    folder_path = os.path.join(root, folder)
    if os.path.exists(folder_path):
        include_files.append((folder_path, folder))

executable = [Executable(main_script, base=base)]

setup(
    name="Asteroids X",
    version="1.0",
    description="Asteroids X application",
    options={
        "build_exe": {
            "packages": ["pygame", "os"],
            "include_files": include_files,  
        }
    },
    executables=executable
)