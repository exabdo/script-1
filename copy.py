import os
from shutil import copy

dir_path = os.path.dirname(os.path.realpath("C:\Users\mnmn\Desktop\New folder"))
print(dir_path)
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.bmp') or file.endswith('.mp3'):
            try:
                copy(str(root + "/" + file), str(dir_path + "/" + "ex pics"))
                print(str(root + "/" + file), str(dir_path + "/" + "ex pics"))
            except:
                pass