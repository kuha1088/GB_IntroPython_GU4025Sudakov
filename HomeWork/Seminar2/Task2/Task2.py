# Задача 12:
# Петя и Катя - брат и сестра. Петя - студент, а Катя - школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных
# числа X и Y (X, Y <= 1 000), а Катя должна их отгадать. Для этого Петя делает две
# подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

from random import randint # Импортируем функцию randint из модуля random

firstNumber = randint(0, 1001) # Придумываем первое число
secondNumber = randint(0, 1001)# Придумываем второе число

sumOfNumbers = firstNumber + secondNumber
productOfNumbers = firstNumber * secondNumber

# Выводим подсказку
print(f'Загадано два числа.\nСумма этих чисел = {sumOfNumbers}.'
    f'\nпроизведение этих чисел = {productOfNumbers}.\n')

# Делаем квадратное уравнение из системы двух уравнений
# sumOfNumbers = firstNumber + secondNumber
# productOfNumbers  =  firstNumber * secondNumber
# productOfNumbers = (sumOfNumbers - secondNumber) * secondNumber
# productOfNumbers = sumOfNumbers * secondNumber - secondNumber ** 2
# secondNumber ** 2 - sumOfNumbers * secondNumber + productOfNumbers

# Уравнение приведенное (старший коэффициент == 1) => искомые числа являются корнями этого уравнения

d = sumOfNumbers ** 2 - 4 * productOfNumbers # Ищем дискрименант

secondNumber = int(sumOfNumbers / 2 + d ** (0.5) / 2)
firstNumber = int(sumOfNumbers / 2 - d ** (0.5) / 2)

print(f'Загаданные числа это: {firstNumber} и {secondNumber}.')