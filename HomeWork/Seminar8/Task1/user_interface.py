# Модуль для взаимодействия с пользователем

import configuration.messages as messages
import controller as control

# Метод выбора действия с программой
def programm_action_choice() -> int:

    user_input = int(input(f'{messages.MSG2}'))

    control.programm_action_determine(user_choice=user_input)

# Метод выбора действий в меню
def menu_action_choice() -> int:

    user_input = int(input(f'{messages.MSG7}'))

    control.menu_action_determine(user_choice=user_input)