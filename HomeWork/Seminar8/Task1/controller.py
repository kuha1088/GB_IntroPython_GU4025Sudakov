# Модуль выбора функции

import configuration.messages as messages
import configuration.pathes as pathes
import user_interface as interface
import contacts_action as action

# Метод определения действия с программой
def programm_action_determine(user_choice: int):

    if user_choice == 1:
        interface.menu_action_choice()
    else:
        print(messages.MSG9)

# Метод определения действий меню
def menu_action_determine(user_choice: int):

    if user_choice == 1:
        action.new_contact(data_file=pathes.CONTACTS_FILE_PATH, messages=(messages.MSG3, messages.MSG4))
    elif user_choice == 2:
        action.search_contact_data(data_file=pathes.CONTACTS_FILE_PATH, message=messages.MSG5)
    elif user_choice == 3:
        action.read_file(data_file=pathes.CONTACTS_FILE_PATH, message=messages.MSG6)
    elif user_choice == 4:
        action.change_contact(data_file=pathes.CONTACTS_FILE_PATH, messages=(messages.MSG10, messages.MSG11))
    elif user_choice == 5:
        action.remove_contact(data_file=pathes.CONTACTS_FILE_PATH, message=messages.MSG12)
