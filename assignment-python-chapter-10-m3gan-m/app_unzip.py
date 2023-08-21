#megan moore
from pathlib import Path
from zipfile import ZipFile
import shutil

path=Path("worldbank_zipfiles")
print("List of directories:")
path_of_directories = [p for p in path.iterdir() if p.is_dir()]
print(path_of_directories)
print("List of .zip files:")
path_of_zipfiles = [p for p in path.rglob("*.zip")]
print(path_of_zipfiles)
#Data_zero = path_of_zipfiles[0]
#print(Data_zero.name)
i=0
for i in range(0,9):
    source_to_unzip = path_of_zipfiles[i]
    target_directory = "worldbank_data"
    with ZipFile(source_to_unzip) as zip:
        zip.extractall(target_directory)
print("done extracting")
