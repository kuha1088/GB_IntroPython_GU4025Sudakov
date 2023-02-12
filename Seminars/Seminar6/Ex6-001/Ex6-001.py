# Задача №39:
# Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве,
# затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве.
# Затем элементы второго массива

# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод:
# 3 3 2 12
# (каждое число вводится с новой строки)

import random

def random_int_list(length, min, max):
    list = []
    for i in range(length):
        list.append(random.randint(min, max))
    return list

length_array_1 = int(input("Введите количество элементов в 1 массиве: "))
list_1 = random_int_list(length_array_1, 0, 20)
print(list_1)
length_array_2 = int(input("Введите количество элементов во 2 массиве: "))
list_2 = random_int_list(length_array_2, 0, 20)
print(list_2)
list_3 = []
for item in list_1:
    if item not in list_2:
        list_3.append(item)
print(f'Вывод: {len(list_3)}')
print(list_3)