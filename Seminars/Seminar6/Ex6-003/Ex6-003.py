# Задача №43:
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список чисел.
# Все числа списка находятся на разных строках.

# Ввод:
# 1 2 3 2 3
# Вывод:
# 2

start_lst = [10, 20, 30, 10, 10, 20]

# 4
count = 0
for i in range(len(start_lst) - 1):
    num_1 = start_lst[i]
    for j in range(i + 1, len(start_lst)):
        num_2 = start_lst[j]
        if num_1 == num_2:
            count += 1
print(count)