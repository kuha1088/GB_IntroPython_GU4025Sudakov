# Задача 30:
# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод:
# 7 2 5
# Вывод:
# 7 9 11 13 15


from User_interface_module import get_user_data

def progression_maker(number_1, number_2, number_3):
    
    list_maker(number_1, number_3)

    if number_3 == 1:
        return number_1
    else:
        return progression_maker(number_1 + number_2, number_2, number_3 - 1)

# 1 + 2 = **3**, 2 ,4
#     3 + 2 = **5**, 2, 3
#         5 + 2 = **7**, 2, 2
#             7 + 2 = **9**, 2, 1
#                         **1**

# Аргумент по умолчанию создаётся один раз.
# Поэтому, если в качестве аргумента по умолчанию выбрать изменяемый тип данных (словарь или список),
# то он будет общим у всех вызовов функции.
# Соответственно, если вы один раз вызовете функцию с аргументом по умолчанию и внутри неё в этот аргумент добавите элементы,
# то они будут там и при следующем вызове этой функции.

# Почему тип данных для result, получаемого как:
# result = some_list.append(next_element)
# None?
# Методы, которые добавляют, вычитают или переставляют элементы на месте и не возвращают конкретный элемент,
# никогда не возвращают сам экземпляр коллекции, а None.

def list_maker(next_element, final_signal, some_list = []):
    
    some_list.append(next_element)
    result = some_list

    if final_signal == 1:
        print (f'Получена последовательность: {str(result)[1:-1]}')

message_for_user_1 = 'Введите первый элемент последовательности: '
message_for_user_2 = 'Введите шаг (разность прогрессии) последовательности: '
message_for_user_3 = 'Введите количество элементов последовательности: '

user_data = get_user_data(msg_1 = message_for_user_1, \
                               msg_2 = message_for_user_2, \
                               msg_3 = message_for_user_3)

(progression_first_element, progression_step, progression_length) = user_data

progression_maker(number_1 = progression_first_element, \
                  number_2 = progression_step, \
                  number_3 = progression_length)