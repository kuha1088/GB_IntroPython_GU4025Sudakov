# Задача 2:
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
#(сдвиг - циклический) на K элементов вправо,
#K - положительное число.
# [1, 2, 3, 4, 5]
# 3
# -> [3, 4, 5, 1, 2]

start_lst = [1, 2, 3, 4, 5]
k = int(input('k: '))
k = -(k%len(start_lst))
result_llst = []

for i in range(len(start_lst)):
    result_llst.append(start_lst[k])
    k += 1

print(result_llst)