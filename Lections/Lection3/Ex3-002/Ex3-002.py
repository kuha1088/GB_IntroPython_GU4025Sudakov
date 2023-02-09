# Функция деления списка и слияния в общий отсортированный список

# Декомпозиция.
# Деление до 1-го элемента ([], [], [] ... [], [], [])
def merge_sort(nums):
    if len(nums) > 1: # делим пока длина списка > 1
        mid = len(nums) // 2 # деление массива на два примерно равной длины
        left = nums[:mid] # первая часть списка
        right = nums[mid:] # вторая часть списка
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0

# Слияние.
# Сортированные спискы складывают в один сортированный.
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

# Добавление крайнего элемента (для нечетной половинки объединяемого списка)
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [1, 5, 6, 9, 8, 7, 2, 1, 55, 2, 4]
merge_sort(list1)
print(list1)