import os
from pathlib import Path
import shutil
import config
from utils import select_directory, ask_to_user_true_false


logger = config.getLogger('venv-clean')


def delete_venv_scripts_folders(directory):
    for root, dirs, files in os.walk(directory):
        for virtual_dir_name in config.virtualized_directories_names:
            if virtual_dir_name in dirs:
                venv_path = os.path.join(root, virtual_dir_name)
                delete_folder(venv_path)


def delete_folder(folder_path):
    user_input = True if config.can_delete else ask_to_user_true_false(None, f"Do U want to delete the folder'{folder_path}'?")
    if user_input:
        shutil.rmtree(folder_path)
        logger.info(f"Deleted: {folder_path}")
        print(f"Deleted: {folder_path}")
    else:
        logger.info(f"Skipped: {folder_path}")
        print(f"Skipped: {folder_path}")


if __name__ == "__main__":
    print('Wait for target dir')
    target_directory: Path = Path(select_directory())
    print(f'target dir: {target_directory}')
    config.can_delete = ask_to_user_true_false(True, 'Delete without asking')
    config.can_delete = ask_to_user_true_false(True, 'Are u sure "delete without asking"')
    print('START')
    delete_venv_scripts_folders(target_directory)

