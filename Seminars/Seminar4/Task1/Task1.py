# Задача 1:
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался.

# H: 3
# e: 1
# l: 3

list_1 = input("Введите слово: ")
temp = list_1[0]
count = 0
dict_1 = {}

for i in range(len(list_1)):
    for j in range(len(list_1)):
        if list_1[i] == list_1[j]:
            count += 1
    dict_1[list_1[i]] = count
    count = 0

print(dict_1)
