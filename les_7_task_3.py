'''
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
'''
import random

M = 5
Size=2*M+1
array = [random.randint(0, 100) for _ in range(Size)]
random.shuffle(array)
fm=0
print(f'Исходный:      {array}')
j=0
mas=[]

while array:
    minimum = array[0]
    for x in array:
        if x < minimum:
            minimum = x
    mas.append(minimum)
    array.remove(minimum)
    j+=1

size_m=j // 2
print(f'Упорядоченный: {mas}')
print(f'Медиана: {mas[size_m]}')


