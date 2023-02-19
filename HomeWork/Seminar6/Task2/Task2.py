# Задача 32:
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод:
# [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод:
# [1, 9, 13, 14, 19]

from Random_collections_maker_module import list_maker
from User_interface_module import get_user_data

def array_check(array, search_range):

    indexes_list = []
    min_border = search_range[0]
    max_border = search_range[1]

    for element_index in range(len(array)):
        if (array[element_index] >= min_border and array[element_index] <= max_border):
            indexes_list.append(element_index)
    
    result = indexes_list
    return result

message_for_user_1 = 'Укажите длину массива: '
message_for_user_2 = 'Укажите минимально возможное значение элемента массива: '
message_for_user_3 = 'Укажите максимально возможное значение элемента массива: '
message_for_user_4 = 'Укажите нижнюю границу поиска элементов массива: '
message_for_user_5 = 'Укажите верхнюю границу поиска элементов массива: '

list_of_messages = message_for_user_1, message_for_user_2, message_for_user_3
array_parameters = get_user_data(messages = list_of_messages)

(checking_arr_length, checking_arr_min, checking_arr_max) = array_parameters

checking_array = list_maker(arr_length = checking_arr_length,\
                          arr_min = checking_arr_min,\
                          arr_max = checking_arr_max)

print()
print(f'Получен массив: {str(checking_array)[1:-1]}')

list_of_messages = message_for_user_4, message_for_user_5
checking_array_search_range = get_user_data(messages = list_of_messages)

print()
print(f'Диапазон поиска: {checking_array_search_range}')

result = array_check(array = checking_array, search_range = checking_array_search_range)
print()
print(f'Индексы элементов массива, значения которых принадлежат заданному диапазону: {result}')