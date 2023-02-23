# Пути к файлам

from pathlib import Path

dir_path = Path(__file__).parents[1]
CONTACTS_FILE_PATH = Path(dir_path,'phone_direction.txt')