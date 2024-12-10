from cx_Freeze import setup, Executable
import os

path = "./asset"
asset_list = os.listdir(path)
asset_list_complete = [os.path.join(path, asset).replace("\\", "/") for asset in asset_list]
print(asset_list_complete)

executables = [Executable("main.py")]
files = {"include_files": asset_list_complete, "packages": ["pygame"]}

setup(
    name="FAT-CAT",
    version="1.0",
    description="FAT-CAT app",
    options={"build_exe": files},
    executables=executables
)