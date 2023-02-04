# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 6
# -> 5

import random

def list_maker_(userNumber):
    
    result = set()

    while(len(result) < userNumber):
        result.add(random.randint(1, 20))
    
    result = list(result)
    return result

def search_(x, list_):
    
    result = int()
    listOfDifferences = []
    k = int()

    for i in range(len(list_)):
        k = abs(list_[i] - x)
        listOfDifferences.append(k)

    minimumDifference = min(listOfDifferences)
    CloserElementIndex = listOfDifferences.index(minimumDifference)
    result = list_[CloserElementIndex]
    return result

print()
elementsNumber = int(input('Введите количество элементов в массиве: '))
print()

listNElements = list_maker_(userNumber = elementsNumber)
print(listNElements)
print()

searchingElement = int(input('Введите искомое значение: '))
print()

result = search_(x = searchingElement, list_ = listNElements)
print(f"Ближайший по величине элемент = {result}")