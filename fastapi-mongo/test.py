import os
from pathlib import Path

directory_in_str = "C:\hp"
createdDirectory = "C:\output"


def change_file_extension_with_pathlib(filename, new_extension):
    path_object = Path(filename)
    new_filename = path_object.with_suffix('.' + new_extension)
    return new_filename

def print_folder_structure(root_folder):
    print(root_folder)
    for root, dirs, files in os.walk(root_folder):

        for folder in dirs:       
            os.makedirs(os.path.join(createdDirectory + root[len(directory_in_str):], folder))

        for file in files:
            filename = change_file_extension_with_pathlib(file,'py')
            completeFolderStructure = os.path.join(createdDirectory + root[len(directory_in_str):], filename)
            open(completeFolderStructure, "w")

print_folder_structure(directory_in_str)