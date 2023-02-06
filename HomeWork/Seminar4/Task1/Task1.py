# Задача 1:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# input 11 6
# first set 2 4 6 8 10 12 10 8 6 4 2
# second set 3 6 9 12 15 18
# output 6 12

import random

def get_user_number(msg, count):

    count += 1    
    print(f"{msg} №{count}: ")
    user_input = int(input())

    result = (user_input, count)
    return result;

def list_maker(userNumber, msg, count):
    
    result = [random.randint(1, 7) for i in range(userNumber)]
    print(f"{msg}{count}: {result}")
    print()
    
    return result

count_get_user_number = 0
message_for_user_1 = 'Введите количество элементов множества'
message_for_user_2 = 'Множество №'

list_1_elements = get_user_number(msg = message_for_user_1, count = count_get_user_number)
(list_1_lenght, count_get_user_number) = list_1_elements
list_1 = list_maker(userNumber = list_1_lenght, msg = message_for_user_2, count = count_get_user_number)

list_2_elements = get_user_number(msg = message_for_user_1, count = count_get_user_number)
(list_2_lenght, count_get_user_number) = list_2_elements
list_2 = list_maker(userNumber = list_2_lenght, msg = message_for_user_2, count = count_get_user_number)

list_1_set = set(list_1)
list_2_set = set(list_2)

common_set = set(list_1) & set(list_2)
result = sorted(common_set)
print(f"Пересечение множеств №{count_get_user_number - 1} и №{count_get_user_number}, отсортированное по возрастанию: {result}")