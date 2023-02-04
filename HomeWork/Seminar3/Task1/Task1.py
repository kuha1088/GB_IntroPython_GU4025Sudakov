# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 3
# -> 1

import random

print()
elementsNumber = int(input('Введите количество элементов в массиве: '))
print()

listNElements = [random.randint(1, 5) for i in range(elementsNumber)]
print(listNElements)
print()
lastElementNumber = len(listNElements) - 1
lastElement = listNElements[lastElementNumber]
print(f"Последний элемент массива = {lastElement}\n")

result = listNElements.count(lastElement)
print(f"Число {lastElement} встречается в массиве {result} раз")