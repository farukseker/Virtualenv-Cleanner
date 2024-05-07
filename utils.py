import tkinter as tk
from tkinter import filedialog
import config


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


print(ask_to_user_true_false(True, '[your question]'))

