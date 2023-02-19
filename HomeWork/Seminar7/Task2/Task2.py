# Задача 36:
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# Ввод:
# print_operation_table(lambda x, y: x * y)
# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36
 

# def print_operation_table(operation: function, num_rows: int = 6, num_columns: int = 6):
# -> tuple[tuple]


from User_interface_module import get_user_data

def index_maker(parameters: tuple) -> tuple[tuple]:
    
    (strings_number, columns_number) = parameters

    indexes_list = []

    for i in range(1, strings_number + 1):
        for j in range(1, columns_number + 1):
            index = (i, j)
            indexes_list.append(index)
    
    result = indexes_list
    return result

def print_operation_table(indexes: list, parameters: tuple, f) -> tuple[int]:
    
    elements_list = []
    (strings_number, columns_number) = parameters

    for element in indexes:
        element = f(element[0], element[1])
        elements_list.append(element)
    
    result = elements_list

    for i in range(strings_number):
        lower_border = columns_number * i
        upper_border = columns_number * i + columns_number
        i += 1
        print()
        for j in range(lower_border, upper_border):
                print(f"{elements_list[j]:^4}", end = "")
    
    return result

message_for_user_1 = 'Укажите количество строк матрицы: '
message_for_user_2 = 'Укажите количество столбцов матрицы: '

list_of_messages = message_for_user_1, message_for_user_2
user_parameters = get_user_data(messages = list_of_messages)

indexes_list = index_maker(parameters=user_parameters)
element_calculate = lambda x, y: x * y
array2d_elements = print_operation_table(indexes=indexes_list, parameters=user_parameters, f=element_calculate)