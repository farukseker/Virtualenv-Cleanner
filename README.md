## venv Cleaner
#### venv Cleaner
This script provides a cleaning service for virtual environments used in projects, specifically targeting virtualenv. Its purpose is to remove certain directories ```[venv, .venv, Scripts]``` found in project directories.

If the user approves the backup option, a backup of the libraries used in the virtual environment is taken before deletion. This allows for recreating the virtual environment directory and continuing the installation if needed in the future.

#### operating instructions

``git clone https://github.com/F4ruk-seker/venv-cleanner.git``

``python main.py`` 

- If you want to be asked before the directories are deleted, check no
- Delete without asking [Y/n] : ``default:Yes``
- If automatic deletion is approved, we ask again because the deletion is a serious process.
- Are u sure "delete without asking" [Y/n] : ``default:Yes``
- We print out the libraries we used in the project we created so we can go back to them again.
- create backup_requirements.text ? [Y/n] : ``default:Yes``

---

#### bring back the project

##### windows cmd

``virtualenv venv``

``cd venv/Scripts/``
``activate``

``cd ..`` ``cd ..``

``pip install -r requirements_backup.txt``

---