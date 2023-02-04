# Задача 3:
# Напишите программу для печати всех уникальных значений в словаре.
# {
#     1: 'V',
#     4: 'C',
#     'ew': 'C'
# }
# -> V, C

import random
import string
string.ascii_letters
'abcde'
#fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

list_1 = [i for i in range(1, 10)]
list_2 = [random.choice(string.ascii_letters) for i in range(1, 10)]
dictionary = dict(zip(list_1, list_2))
print()
print(f"Словарь: {dictionary} \n")
print(f"Уникальные значения словаря: {set(dictionary.values())}")