import os
import shutil

# Step 2 - Ask for the folder to organize
folder = input("Enter the folder path to organize: ")

# Step 3 - Check that the folder actually exists
if not os.path.exists(folder):
    print("Error: The folder path you entered does not exist. Please try again.")
else:
    # Step 4 - Get the list of files in the folder
    files = os.listdir(folder)

    # Step 5 - Set up counters
    images_moved = 0
    documents_moved = 0
    videos_moved = 0
    others_moved = 0

    # Step 6 - Create the destination subfolders (only if they don't exist)
    images_path = os.path.join(folder, "Images")
    documents_path = os.path.join(folder, "Documents")
    videos_path = os.path.join(folder, "Videos")
    others_path = os.path.join(folder, "Others")

    if not os.path.exists(images_path):
        os.mkdir(images_path)
    if not os.path.exists(documents_path):
        os.mkdir(documents_path)
    if not os.path.exists(videos_path):
        os.mkdir(videos_path)
    if not os.path.exists(others_path):
        os.mkdir(others_path)

    # Step 7 - Loop through every file and sort it
    for item in files:
        # Skip the four category folders so we don't sort a folder into itself
        if item == "Images" or item == "Documents" or item == "Videos" or item == "Others":
            continue

        full_item_path = os.path.join(folder, item)

        # Skip anything that is a folder rather than a file
        if os.path.isdir(full_item_path):
            continue

        # Use a lowercase copy of the filename so .JPG matches .jpg too
        lower_name = item.lower()

        # Decide which category the file belongs to
        if lower_name.endswith(".jpg") or lower_name.endswith(".jpeg") or lower_name.endswith(".png") or lower_name.endswith(".gif"):
            destination = images_path
            images_moved += 1
            label = "Images/"
        elif lower_name.endswith(".pdf") or lower_name.endswith(".docx") or lower_name.endswith(".txt") or lower_name.endswith(".pptx"):
            destination = documents_path
            documents_moved += 1
            label = "Documents/"
        elif lower_name.endswith(".mp4") or lower_name.endswith(".mov") or lower_name.endswith(".avi"):
            destination = videos_path
            videos_moved += 1
            label = "Videos/"
        else:
            destination = others_path
            others_moved += 1
            label = "Others/"

        # Step 8 - Actually move the file
        shutil.move(full_item_path, os.path.join(destination, item))

        # Step 9 - Print what happened, file by file
        print("Moved: " + item + " -> " + label)

    # Step 10 - Print a final summary
    total_moved = images_moved + documents_moved + videos_moved + others_moved

    print("")
    print("----- FOLDER SUMMARY -----")
    print("Images moved: " + str(images_moved))
    print("Documents moved: " + str(documents_moved))
    print("Videos moved: " + str(videos_moved))
    print("Others moved: " + str(others_moved))
    print("Total files organized: " + str(total_moved))
