import os
import shutil

path = 'E:/Export Files/path'
new_path = 'E:/Export Files/path/new_folder'

some_text = "some_text"

for file_name in os.listdir(path):
    if some_text in file_name:
        file_path = os.path.join(path, file_name)
        new_file_path = os.path.join(new_path, file_name)
        shutil.move(file_path, new_file_path)
        print("Moved file: ",file_name)
