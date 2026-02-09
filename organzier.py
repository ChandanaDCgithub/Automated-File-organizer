def organize_files():
    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if file.lower().endswith(tuple(extensions)):
                    destination = os.path.join(SOURCE_FOLDER, folder, file)
                    shutil.move(file_path, destination)
                    logging.info(f"Moved {file} to {folder}")
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(SOURCE_FOLDER, "Others")
                if not os.path.exists(other_path):
                    os.makedirs(other_path)
                destination = os.path.join(other_path, file)
                shutil.move(file_path, destination)
                logging.info(f"Moved {file} to Others")
