from pathlib import Path
import logging


DEBUG: bool = True

BASE_DIR: Path = Path(__file__).resolve().parent

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='venv_cleaner.log', filemode='w')
getLogger = logging.getLogger

virtualized_directories_names: list[str] = [
    'venv',
    'Scripts'
]
# can_delete: bool = input('delete without asking y/s').lower() == 'y'
can_delete: bool = True

