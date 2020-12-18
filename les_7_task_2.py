'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''
import random


def m_sort(array, k, i, mas):
    while i < len(mas):
        array[k] = mas[i]
        i = i + 1
        k = k + 1
    return array


def compare_sort(array):
    if len(array) < 2:
        return array
    left = compare_sort(array[:len(array) // 2])
    right = compare_sort(array[len(array) // 2:len(array)])
    i = 0
    k = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            array[k + 1] = right[i]
            i += 1
        else:
            array[k] = right[j]
            array[k + 1] = left[i]
            j += 1
        k = k + 1

    array = m_sort(array, k, i, left)
    array = m_sort(array, k, j, right)

    return array


array = [random.uniform(0, 50) for _ in range(50)]
random.shuffle(array)
print(f'Input: {array}')
print(f'Sorted: {compare_sort(array)}')
