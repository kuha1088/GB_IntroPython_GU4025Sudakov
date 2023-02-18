# Задача №49:
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# S = a * b, a != b

# list_1 = [1, 2]
# list_2 = [3, 4, 1]

# print([(x,y) for x in list_1 for y in list_2 if x != y])

# Вариант 1:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] 
# orbits_elliptic = [item for item in orbits if item [0] != item [1]]
# max_elliptic_length = max(list(map(lambda x: math.pi*x[0]*x[1], orbits_elliptic)))
# longest_orbit = [item for item in orbits_elliptic if math.pi*item[0]*item[1] == max_elliptic_length]

# print('{:.4f}'.format(max_elliptic_length))
# print(*longest_orbit)

# Вариант 2:
# def find_farthest_orbit(orbits):
#     return max(orbits, key=lambda x:(x[0] != x[1])*x[0]*x[1])

# orbits = [(1, 3), (2.5, 10), (7, 2), (6,6)]
# print(find_farthest_orbit(orbits))
# print(orbits.index(find_farthest_orbit(orbits)))

# Вариант 3:
# def find_farthest_orbit(orbits):
#     # return max(orbits, key=lambda x:(x[0] != x[1])*x[0]*x[1])
#     s_orbits = list(map(lambda x: x[0]*x[1] if x[0] != x[1] else 0, orbits))
#     max_s_i = s_orbits.index(max(s_orbits))
#     return orbits[max_s_i]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6,6), (40, 40)]
# print(*find_farthest_orbit(orbits))

# Вариант 4:
def find_farthest_orbit(orbits):
    dict_s = {x[0]*x[1]: x for x in orbits if x[0] != x[1]}
    return dict_s[max(dict_s)]


orbits = [(1, 3), (2.5, 10), (7, 2), (6,6), (40, 40)]
print(*find_farthest_orbit(orbits))