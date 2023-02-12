# Задача №45:
# Два различных натуральных числа n и m называются дружественными, если
# сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 10^5.
# Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

# Ввод:
# 300
# Вывод:
# 220 284

number_friend_check = int(input('Введите число для проверки:'))

def divisors_sum (input_number):
    sum = 0
    for i in range (1, input_number):
        if input_number % i == 0:
            sum += i
    return sum

def friendly_pairs (input_number):
    for i in range (2, input_number + 1):
        j = divisors_sum (i)
        if i <= (input_number) and j <= (input_number):
            print(i, j)

friendly_pairs(number_friend_check)


# n = int(input())
# list_1 = list()

# for i in range(n):
#     summa = 0
#     for j in range(1, i // 2 + 1):
#         if i % j == 0:
#             summa += j
#     list_1.append(tuple([i, summa]))


# for i in range(len(list_1)):
#     for j in range(i, len(list_1)):
#         if (i != j) and (list_1[i][0]) == (list_1[j][1]) and (list_1[i][1]) == (list_1[j][0]):
#             print(*list_1[i])