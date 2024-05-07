import shutil
import tkinter as tk
from tkinter import filedialog
import config
import os


def select_directory():
    logger = config.getLogger('utils-select-directory')

    root = tk.Tk()
    root.withdraw()

    directory = filedialog.askdirectory()

    if directory:
        logger.info(f'user-select {directory}')
        return directory
    else:
        logger.critical('user not selected a dir')
        raise "dir not selected."


def ask_to_user_true_false(default: bool | None, ask_message: str) -> bool:
    """
    ask_to_user_true_false(True, '[your question]')

    :param ask_message:str:[your question]

    :param default:bool:True
    [your question] [Y/n] : (user input)
    True
    [your question] [Y/n] :(user input:y)
    :return True
    [your question] [Y/n] :(user input:n)
    False
    ----------------------------
    :param default:bool|None:None

    [your question] [Y/N] :(user input:test)
    [your question] [Y/N] :(user input: )
    [your question] [Y/N] :(user input:e)
    [your question] [Y/N] :(user input:y)
    True
    """

    default_msg = '[Y/N]' if type(default) is not bool else f'[{'Y' if default else 'y'}/{'n' if default else 'N'}]'

    def ask():
        answer = input(f"{ask_message} {default_msg} :")
        if answer.lower() == 'y':
            return True
        elif answer.lower() == 'n':
            return False
        else:
            if type(default) is not bool:
                return ask()
            else:
                return default
    return ask()


def requirements_txt_create(root_dir, venv_path):
    logger = config.getLogger('utils-requirements-txt-create')
    try:

        requirements_file = os.path.join(root_dir, config.backup_requirements_text_name)
        if not os.path.exists(requirements_file):
            with open(requirements_file, 'w') as f:
                pip_freeze_command = f"{venv_path}\\Scripts\\pip freeze"
                pip_freeze_output = os.popen(pip_freeze_command).read()
                f.write(pip_freeze_output)
                logger.info(f"'requirements.txt' dosyası {root_dir} altında oluşturuldu.")
    except Exception as exception:
        logger.critical(exception)

def delete_folder(folder_path):
    logger = config.getLogger('utils-delete-folder')
    try:
        user_input = True if config.can_delete else ask_to_user_true_false(None,
                                                                           f"Do U want to delete the folder'{folder_path}'?")
        if user_input:
            shutil.rmtree(folder_path)
            logger.info(f"Deleted: {folder_path}")
            print(f"Deleted: {folder_path}")
        else:
            logger.info(f"Skipped: {folder_path}")
            print(f"Skipped: {folder_path}")
    except Exception as exception:
        logger.critical(exception)

