# Задача №41:
# Дан массив, состоящий из целых чисел. Напишите программу,
# которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел.

# Ввод:
# 5
# 1 2 3 4 5
# Вывод:
# 0
# Ввод:
# 5
# 1 5 1 5 1
# Вывод:
# 2
# (каждое число вводится с новой строки)

import random

def list_maker(number):
    
    result = [random.randint(1, 5) in range(number)]
    print(result)
    return result

def check_of_list(checking_list):

    result = int()

    for i in range(1, len(checking_list) - 1):
        if (checking_list[i] > checking_list[i - 1] and checking_list[i] > checking_list[i + 1]):
            result += 1
    
    return result

print()
user_number = int(input('Введите количество элементов в массиве: '))
print()
list_1 = list_maker(number = user_number)
result = check_of_list(checking_list = list_1)
print(f'Количество элементов, удовлетворяющих условию: {result}')
