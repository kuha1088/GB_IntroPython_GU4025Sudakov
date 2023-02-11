# Задача №33:
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия,
# но наоборот:
# все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random

def list_maker():
    
    result = [random.randint(1, 5) for i in range(10)]
    
    return result

def change_list(list_marks):
    
    max_mark = max(list_marks)
    print(f'Максимальная оценка Василия: {max_mark}')
    min_mark = min(list_marks)
    print(f'Минимальная оценка Василия: {min_mark}')

    for i in range(len(list_marks)):
        if list_marks[i] == max_mark:
            list_marks[i] = min_mark

    return list_marks

list_1 = list_maker() 

print()
print(f'Первоначальные оценки Василия: {str(list_1)[1:-1]}')

list_2 = change_list(list_marks  = list_1)
print(f'Новые оценки Василия: {str(list_2)[1:-1]}')