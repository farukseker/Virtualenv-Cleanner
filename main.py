import os
import shutil

def delete_venv_scripts_folders(directory):
    for root, dirs, files in os.walk(directory):
        if 'venv' in dirs:
            venv_path = os.path.join(root, 'venv')
            delete_folder(venv_path)

        if 'scripts' in dirs:
            scripts_path = os.path.join(root, 'Scripts')
            delete_folder(scripts_path)

def delete_folder(folder_path):
    user_input = input(f"Do you want to delete the folder '{folder_path}'? (y/n): ").lower()
    if user_input == 'y':
        shutil.rmtree(folder_path)
        print(f"Deleted: {folder_path}")
    else:
        print(f"Skipped: {folder_path}")

if __name__ == "__main__":
    target_directory = os.getcwd()
    delete_venv_scripts_folders(target_directory)
