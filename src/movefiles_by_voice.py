import os
import cv2
import time
import speech_recognition as sr

# Define the folder path where the images are located
folder_path = '/home/gourav/Downloads/lakmeimages'
files = os.listdir(folder_path)
files = [f for f in files if f.endswith('.jpg') or f.endswith('.png')]

# Iterate over all the files in the folder
for ind, file_name in enumerate(files):
    # Read the image
    img_path = os.path.join(folder_path, file_name)
    img = cv2.imread(img_path)

    # Show the image
    window_name = file_name
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(file_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    try:
        # Take voice input
        r = sr.Recognizer()
        with sr.Microphone() as source:
            os.system('cls' if os.name == 'nt' else 'clear')
            ln = len(files) - ind
            print(f'Images Left:{ln}')
            print('Say the folder name:')
            audio = r.listen(source)

        # Convert voice input to text
        folder_name = r.recognize_google(audio)
        print(f"result: {folder_name}")
        # Rename/move the image to the folder with the given name
        new_folder_path = os.path.join(folder_path, folder_name)
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
        new_img_path = os.path.join(new_folder_path, file_name)
        os.rename(img_path, new_img_path)
    except: pass