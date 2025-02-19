import os
from pathlib import Path
import config
from utils import select_directory, ask_to_user_true_false, requirements_txt_create, delete_folder


logger = config.getLogger('venv-clean')


def delete_venv_scripts_folders(directory):
    for root, dirs, files in os.walk(directory):
        for virtual_dir_name in config.virtualized_directories_names:
            if virtual_dir_name in dirs:
                venv_path = os.path.join(root, virtual_dir_name)
                if config.create_backup_requirements_text or not virtual_dir_name.startswith('__'):
                    requirements_txt_create(root, venv_path)
                delete_folder(venv_path)


def main():
    print('Wait for target dir')
    target_directory: Path = Path(select_directory())
    if target_directory:
        print(f'target dir: {target_directory}')
        config.can_delete = ask_to_user_true_false(True, 'Delete without asking')
        if config.can_delete:
            config.can_delete = ask_to_user_true_false(True, 'Are u sure "delete without asking"')
        config.create_backup_requirements_text = ask_to_user_true_false(config.create_backup_requirements_text,
                                                                        'create backup_requirements.text ?')

        if ask_to_user_true_false(True, 'Do you want to delete cache files if there are any?'):
            config.virtualized_directories_names.append('__pycache__')
        
        print('START')
        delete_venv_scripts_folders(target_directory)
        print('END')


if __name__ == "__main__":
    main()

