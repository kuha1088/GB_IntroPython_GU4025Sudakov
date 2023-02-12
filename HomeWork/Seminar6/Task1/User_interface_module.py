# Класс функций для взаимодействия с пользователем

# Метод проверки правильности ввода (ожидается ввод целого числа)
def get_user_data_check(msg_1: str, msg_2: str, count: int) -> tuple[int, int]:
    
    count += 1

    print(f"{msg_1}{count}{msg_2}", end = '')
    
    while(True):
        try:
            user_input = int(input())
            if (type(user_input) == int):
                result = (user_input, count)
                return(result)
            else:
                raise ValueError
        except ValueError:
            print("Введенное значение не соответствует условиям задачи, повторите ввод.")

# Метод получения данных от пользователя с выводом запроса(-ов) в виде текста
def get_user_data(msg_1: str, msg_2: str, msg_3: str) -> tuple[int, int, int]:
    
    print()
    user_data_1 = int(input(msg_1))
    user_data_2 = int(input(msg_2))
    user_data_3 = int(input(msg_3))
    print()

    result = (user_data_1, user_data_2, user_data_3)
    return result