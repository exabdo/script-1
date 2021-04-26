# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

##########################################################################################
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  #+ Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import os
from PIL import Image, ImageStat

image_folder = r'C:\Users\mnmn\Pictures\Screenshots\New folder'
image_files = [_ for _ in os.listdir(image_folder) if _.endswith('png')]

duplicate_files = []

for file_org in image_files:
    if not file_org in duplicate_files:
        image_org = Image.open(os.path.join(image_folder, file_org))
        pix_mean1 = ImageStat.Stat(image_org).mean

        for file_check in image_files:
            if file_check != file_org:
                image_check = Image.open(os.path.join(image_folder, file_check))
                pix_mean2 = ImageStat.Stat(image_check).mean

                if pix_mean1 == pix_mean2:
                    ################  # duplicate_files.append((file_org))
                    duplicate_files.append((file_check))

print(list(dict.fromkeys(duplicate_files)))

# print(duplicate_files)
# print(image_files)

# Python program to print list
# using for loop
import send2trash

# printing the list using loop
for x in range(len(list(dict.fromkeys(duplicate_files)))):
    dele = (list(dict.fromkeys(duplicate_files))[x])
    filepath = r"C:\Users\mnmn\Pictures\Screenshots\New folder\{}".format(dele)
    send2trash.send2trash(filepath)
    print(dele)
