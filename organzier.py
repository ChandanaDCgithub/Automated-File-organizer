import os
import shutil

# CHANGE THIS PATH to the folder you want to organize
SOURCE_FOLDER = "sample_folder"

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Audio": [".mp3", ".wav"]
}

def create_folders():
    for folder in FILE_TYPES.keys():
        path = os.path.join(SOURCE_FOLDER, folder)
        if not os.path.exists(path):
            os.makedirs(path)

def organize_files():
    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if file.lower().endswith(tuple(extensions)):
                    shutil.move(file_path, os.path.join(SOURCE_FOLDER, folder, file))
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(SOURCE_FOLDER, "Others")
                if not os.path.exists(other_path):
                    os.makedirs(other_path)
                shutil.move(file_path, os.path.join(other_path, file))

if __name__ == "__main__":
    create_folders()
    organize_files()
    print("Files organized successfully!")

