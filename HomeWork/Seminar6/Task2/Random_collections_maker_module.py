# Класс функций для создания рандомных колеекций

# Метод генерации заданной длины массива целых чисел заданном диапазоне
# (ожидается ввод длины массива и границ диапазона)
import random

def list_maker(arr_length: int, arr_min: int, arr_max: int) -> list[int]:
    
    result = [random.randint(arr_min, arr_max) for i in range(arr_length)]
    
    return result