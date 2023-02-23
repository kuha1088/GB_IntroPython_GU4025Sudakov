# Модуль для действий с контактами

import os
from tabulate import tabulate

# Метод добавления нового контакта
def new_contact(data_file: str, messages: tuple[str]) -> str:

    (message_1, message_2) = messages

    contact_name = input(message_1)
    contact_phone = input(message_2)

    with open(data_file, 'a', encoding="utf-8") as working_file:
        working_file.write(f'\n{contact_name}: {contact_phone}')
        print ('Контакт добавлен')
   
    from main import invitation
    invitation()

# Метод для изменения данных контакта
def change_contact(data_file: str, messages: tuple[str]) -> str:

    (message_1, message_2) = messages

    changing_data_old = input(message_1)
    changing_data_new = input(message_2)

    with open(data_file, 'r', encoding="utf-8") as working_file:
        data = working_file.read()
    with open(data_file, 'w', encoding="utf-8") as working_file:
        data = data.replace(changing_data_old, changing_data_new)
        working_file.write(data)
        
        print ('Данные заменены')
   
    from main import invitation
    invitation()

def remove_contact(data_file: str, message: str) -> str:

    removing_data = input(message)

    with open(data_file, 'r', encoding="utf-8") as working_file:
        data = working_file.readlines()
    with open(data_file, 'w', encoding="utf-8") as working_file:
        for line in data:
            if removing_data not in line.strip('\n'):
                working_file.write(line)
        
        print ('Данные удалены')
   
    from main import invitation
    invitation()

# Метод для поиска информации в справочнике
def search_contact_data(data_file: str, message: str) -> str:

    search_by = input(message)

    with open(data_file, 'r', encoding="utf-8") as working_file:
        contacts_list = []
        for line in working_file:
            if search_by in line:
                line = line.split(':')
                contacts_list.append(line)
        result = contacts_list
        print(tabulate(result, headers = ['Name', 'Phone'], tablefmt='orgtbl'))
    
    from main import invitation
    invitation()

# Метод для вывода построчно файла
def read_file(data_file: str, message: str) -> str:
    if os.path.exists(data_file):
        with open(data_file, 'r', encoding="utf-8") as working_file:
            contacts_list = []
            for line in working_file:
                line = line.split(':')
                contacts_list.append(line)
            result = contacts_list
            print(tabulate(result, headers = ['Name', 'Phone'], tablefmt='orgtbl'))
    else:
        print(message)

    from main import invitation
    invitation()