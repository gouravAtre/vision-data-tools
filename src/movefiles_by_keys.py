# -- coding: utf-8 --
'''
Created on 17-March-2023 22:10
Project: vision-data-tools 
@author: Gourav Atre
@email: gouravkumar1815@gmail.com

Purpose: To take image files from a folder 
        and divide them into specific sub folders in one click
        to whichever category they belong.

Process brief: 
    > All files are listed from the given folder. 
    > one by one all files will be displayed if the file endswith jpg or png or jpeg.
    > then you have to press a key (any key), just keeping in mind -> 
    > that image file will be moved to the folder named after the key pressed. 
      for ex: if key "a" is pressed then the image will be moved to folder named a 
              which will be inside the original given folder.

'''


import os
import cv2
import time


def main(folder_path):
    # Define the folder path where the images are located
    files = os.listdir(folder_path)
    files = [f for f in files if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')]

    # Iterate over all the files in the folder
    for ind, file_name in enumerate(files):
        # Read the image
        img_path = os.path.join(folder_path, file_name)
        img = cv2.imread(img_path)

        # Show the image
        window_name = file_name
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(window_name, 700, 700)
        cv2.imshow(file_name, img)
        key = cv2.waitKey()
        

        try:
            # Take text input
            folder_name = str(chr(key))

            print(f'"{file_name}" : "{folder_name}"')
            # Rename/move the image to the folder with the given name
            new_folder_path = os.path.join(folder_path, folder_name)

            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
            new_img_path = os.path.join(new_folder_path, file_name)
            os.rename(img_path, new_img_path)

        except Exception as e: print(e)

        cv2.destroyAllWindows()


if __name__ == "__main__":
    folder_path = "/home/gourav/Downloads/disha_nonShelf_testImages"
    main(folder_path)