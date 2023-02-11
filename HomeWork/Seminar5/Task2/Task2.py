# Задача 2:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

from User_interface_module import get_user_number

def summary(number_1, number_2):

    if number_2 == 0:
        return number_1
    else:
        return summary(number_1 + 1, number_2 - 1)

count_get_user_number = 0
message_for_user_1 = 'Введите '
message_for_user_2 = '-е число: '

print()
first_user_number_elements = get_user_number(msg_1 = message_for_user_1, msg_2 = message_for_user_2 ,count = count_get_user_number)
(first_user_number, count_get_user_number) = first_user_number_elements
second_user_number_elements = get_user_number(msg_1 = message_for_user_1, msg_2 = message_for_user_2 ,count = count_get_user_number)
(second_user_number, count_get_user_number) = second_user_number_elements
print()

result = summary(number_1 = first_user_number, number_2 = second_user_number)
print(f'Сумма чисел {first_user_number} и {second_user_number} = {result}')
