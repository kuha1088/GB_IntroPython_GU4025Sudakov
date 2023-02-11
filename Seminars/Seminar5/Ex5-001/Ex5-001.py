# Задача №31:
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13

def fibonacci(a):
    if a == 1 or a == 2:
        return 1
    else:
        return fibonacci(a-1) + fibonacci(a-2)

fibonacci_input = int(input('Введите номер числа в посследовательности Фибоначчи:'))
print(fibonacci(fibonacci_input))