# Задача 6:
# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым номером называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 - счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

ticketNumber = int(input('Введите номер билета: '))
firstPartNumbersSum = 0
lastPartNumbersSum = 0
firstPartNumbers = int(ticketNumber//1000)

while(ticketNumber//1000 != 0):
    temp = ticketNumber % 10
    lastPartNumbersSum += temp
    ticketNumber = ticketNumber // 10
print(lastPartNumbersSum)

while(firstPartNumbers != 0):
    temp = firstPartNumbers % 10
    firstPartNumbersSum += temp
    firstPartNumbers = firstPartNumbers // 10
print(firstPartNumbersSum)

if(firstPartNumbersSum == lastPartNumbersSum):
    print('Билет счастливый')
else:
    print('Билет не счастливый')