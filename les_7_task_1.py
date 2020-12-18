'''
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
'''
import random


def bubble_mod(array):
    n = 1
    ln = len(array)
    while n < ln:
        for i in range(ln - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1

    return array


array = [random.randint(-100, 99) for _ in range(100)]
random.shuffle(array)  # перемешивает значения в массиве
print(array)
print(bubble_mod(array))
