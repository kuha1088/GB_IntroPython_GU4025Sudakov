# Задача 4:
# Петя, Катя и Сережа делают журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок , если известно,
# Что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем
# Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

commonCraneNumber = int(input('Введите общее число журавликов: '))
craneNumberPete = 0
craneNumberSerge = 0
craneNumberKate = 0

# commonCraneNumber == craneNumberPete + craneNumberSerge + craneNumberKate
# craneNumberPete == craneNumberSerge
# craneNumberKate == (craneNumberPete + craneNumberSerge)*2 = craneNumberPete*4
# commonCraneNumber == craneNumberPete*2 + craneNumberPete*4 = craneNumberPete*6

craneNumberPete = int(commonCraneNumber/6)
craneNumberSerge = int(commonCraneNumber/6)
craneNumberKate = int((commonCraneNumber/6)*4)

print(f'Число журавлей, сделанных Петром {craneNumberPete}')
print(f'Число журавлей, сделанных Екатериной {craneNumberKate}')
print(f'Число журавлей, сделанных Сергеем {craneNumberSerge}')