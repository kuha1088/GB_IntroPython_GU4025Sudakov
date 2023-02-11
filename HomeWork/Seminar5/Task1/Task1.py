# Задача 1:
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def production(number, power):
    
    if power == 1:
        return number
    else:
        return (number * production(number, power - 1))

print()
powered_number = int(input('Введите число возводимое в степень: '))
power_for_number = int(input('Введите степень, в которую необходимо возвести число: '))
print()

result = production(number = powered_number, power = power_for_number)
print(f'Число {powered_number} в степени {power_for_number} = {result}')