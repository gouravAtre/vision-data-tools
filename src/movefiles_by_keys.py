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
import numpy as np


def main(folder_path):
    # Define the folder path where the images are located
    files = os.listdir(folder_path)
    files = [f for f in files if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')]
    total_n_files = len(files)
    last_file = {"filepath":"",
                 "folder_name": ""}
    # Iterate over all the files in the folder
    for ind, file_name in enumerate(files):
        # Read the image
        img_path = os.path.join(folder_path, file_name)
        img = cv2.imread(img_path)

        # print(img.shape)
        tx, ty = 10, 20
        border_thickness = 1
        thickness=1
        font = cv2.FONT_HERSHEY_DUPLEX
        font_sz = 0.5
        
        # For weighted img fullness
        cv2.putText(img, f"{total_n_files-ind}", (tx - border_thickness, ty - border_thickness), font, font_sz, (0, 0, 0), thickness+border_thickness, cv2.LINE_AA)
        cv2.putText(img, f"{total_n_files-ind}", (tx, ty), font, font_sz, (255, 255, 255), thickness)
        # Show the image
        window_name = file_name
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(window_name, 700, 700)
        cv2.imshow(window_name, img)
        key = cv2.waitKey()
        
        # Close the window if 'Esc' key is pressed
        if key == 27:
            break

        if str(chr(key)) == "z":
            if last_file["filepath"] == "":
                # Create a blank image with white background
                image = 255 * np.ones((700, 700, 3), dtype=np.uint8)

                # Write the text on the image
                cv2.putText(image, "Can't undo on first image!", (10, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
                cv2.putText(image, "Press any key to continue...", (10, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
                # Display the image
                cv2.imshow("Blank Image", image)
                cv2.waitKey(0)
                cv2.destroyWindow(window_name)
                
                # Show the image
                window_name = file_name
                cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
                cv2.resizeWindow(window_name, 700, 700)
                cv2.imshow(file_name, img)
                key = cv2.waitKey()
                # Close the window if 'Esc' key is pressed
                if key == 27:
                    break

            else:
                # Show the image
                undo_image = cv2.imread(last_file["filepath"])
                window_name = "Undo window"
                cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
                cv2.resizeWindow(window_name, 700, 700)
                cv2.imshow(window_name, undo_image)
                key = cv2.waitKey()
                # try:
                # Take text input
                new_folder_name = str(chr(key))
                last_dirname = os.path.dirname(last_file["filepath"])
                last_dirname_replacement = last_dirname.rstrip("/")[:-1] + new_folder_name
                undo_filename = last_file["filepath"].replace(last_dirname, last_dirname_replacement)

                print(f'Undo :: "{undo_filename}" : "{new_folder_name}"')

                os.makedirs(os.path.dirname(undo_filename), exist_ok=True)
                os.rename(last_file["filepath"], undo_filename)
                cv2.destroyWindow(window_name)
                
                                                                            
                # Show the image
                window_name = file_name
                cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
                cv2.resizeWindow(window_name, 700, 700)
                cv2.imshow(file_name, img)
                key = cv2.waitKey()
                # Close the window if 'Esc' key is pressed
                if key == 27:
                    break

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

            last_file["filepath"] = new_img_path
            last_file["folder_name"] = folder_name

        except Exception as e: print(e)

        cv2.destroyAllWindows()


if __name__ == "__main__":
    folder_path = "enter the folder path here"
    main(folder_path)
