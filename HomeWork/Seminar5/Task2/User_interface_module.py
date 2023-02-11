# Класс функций для взаимодействия с пользователем

# Метод проверки правильности ввода (ожидается ввод целого числа)
def get_user_number(msg_1: str, msg_2: str, count: int) -> tuple[int, int]:
    
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