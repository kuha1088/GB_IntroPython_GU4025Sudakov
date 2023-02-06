# Задача 2:
# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

# input 4
# 1 2 3 4
# output 9

# **ОГОВОРКА ПО УСЛОВИЮ ЗАДАЧИ:**
# В примере ввод/вывод после ввода "4" не могло получиться "9".
# "9" могло получиться только для 3-го куста в качестве стартового. 
# Количество ягод на кустах в примере соответствует порядковому номеру.
# Если принять, что номер куста = количество ягод на кусте, то максимальное число ягод
# всегда будет равно сумме порядковых номеров последних трех кустов.
# Задача сведется к определению количества кустов.
# **Поэтому примем, что количество ягод на кусте != порядковому номеру куста и распределяется рандомно**
# (не в порядке возрастания или убывания номера куста и т.д.)**

import random

def blueberry_field_maker(msg):

    number_of_bushes = random.randint(5, 15)
    bushes = [i for i in range(1, number_of_bushes)]
    bush_crop = [random.randint(1, 10) for i in range(number_of_bushes)]

    result_field = dict(zip(bushes, bush_crop))
    print(f"{msg}{result_field}")

    result = (number_of_bushes, result_field)
    return result

def harvester_position_maker(msg, number):

    result = random.randint(1, number)
    print(f"{msg}{result}")
    return result

def harveter_production_analyze(position, field):

    result = field[position] + field[position + 1] + field[position - 1]
    return result

message_for_user_1 = 'Анализируемое поле: '
message_for_user_2 = 'Позиция комбайна - куст №'
field_elements = blueberry_field_maker(msg = message_for_user_1)
(number_of_bushes, result_field) = field_elements
blueberry_field = result_field
harvester_position = harvester_position_maker(msg = message_for_user_2, number = number_of_bushes)

result = harveter_production_analyze(position = harvester_position, field = blueberry_field)
print(f"Объем ягод, который сможет собрать комбайн: {result}")
