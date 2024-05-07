import os
from pathlib import Path
import shutil
import config
from utils import select_directory


logger = config.getLogger('venv-clean')


def delete_venv_scripts_folders(directory):
    for root, dirs, files in os.walk(directory):
        for virtual_dir_name in config.virtualized_directories_names:
            if virtual_dir_name in dirs:
                venv_path = os.path.join(root, virtual_dir_name)
                delete_folder(venv_path)


def delete_folder(folder_path):
    user_input = True if config.can_delete else input(f"Do U want to delete the folder'{folder_path}'? (y/n): ").lower()
    if user_input == 'y':
        shutil.rmtree(folder_path)
        print(f"Deleted: {folder_path}")
    else:
        print(f"Skipped: {folder_path}")


if __name__ == "__main__":
    target_directory = Path(select_directory())
    print(target_directory)
    # delete_venv_scripts_folders(target_directory)
