import os
import sys

target_folder = input("Enter the path of the folder to organize: ")

if not os.path.exists(target_folder):
    print("Error: The folder path you entered does not exist. Please try again.")
else:
    print("Organizing files in folder: " + target_folder)
    # Step 4 - Get the list of files in the folder
    files = os.listdir(target_folder)

    images_moved = 0
    documents_moved = 0
    videos_moved = 0
    others_moved = 0
    total_files = 0

    images_path = os.path.join(target_folder, "Images")
    documents_path = os.path.join(target_folder, "Documents")
    videos_path = os.path.join(target_folder, "Videos")
    others_path = os.path.join(target_folder, "Others")
    total_files = os.pathjoin(target_folder, "Total_Files")

    if not os.path.exists(images_path):
        os.mkdir(images_path)
    if not os.path.exists(documents_path):
        os.mkdir(documents_path)
    if not os.path.exists(videos_path):
        os.mkdir(videos_path)
    if not os.path.exists(others_path):
        os.mkdir(others_path)