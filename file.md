You can filter the files based on a specific text in the file name, and move them to another folder using python.
Here's an example using the os and shutil modules:

```python

import os
import shutil

path = '/path/to/original/folder/'
new_path = '/path/to/new/folder/'

for file_name in os.listdir(path):
    if "some_text" in file_name:
        file_path = os.path.join(path, file_name)
        new_file_path = os.path.join(new_path, file_name)
        shutil.move(file_path, new_file_path)
        print("Moved file: ",file_name)


```text
In this example, the script first defines the path of the original folder and the new folder. Then it uses the os.listdir() function to list all the files in the original folder. It iterates over the list of files and filters the files based on whether they contain the text "some_text" in their file name using an if statement. Then it uses the os.path.join() function to construct the file path of the original file and the new file. The shutil.move() function is used to move the file from the original folder to the new folder. The print() function is used to print the name of the moved file.
Please note that the shutil.move() function will overwrite the file with the same name in the new folder, so it's better to take caution when using the same file name in the new folder.
It's also worth noting that using the os.path.join() function is a more robust way to construct file paths, as it can handle different operating systems that use different path separators.
