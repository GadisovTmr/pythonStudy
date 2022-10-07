# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import random

def random_list_without_int (a):
    spisok = []
    for i in range(a):
        spisok.append(round(random.uniform(0, 10),2))
    print(spisok)
    for i in range(len(spisok)):
        spisok[i] = round(spisok[i]%1,2)
    print(spisok)
    return spisok

def min_max_diff_in_list (list):
    min = list[0]
    max = list[0]
    differ = 0
    for i in range(len(list)):
        if min > list[i]:
            min = list[i]
        if max < list[i]:
            max = list[i]
    differ = max - min
    print(f'Min = {min}, Max = {max}, Difference = {round(differ,2)}')
    return min, max, differ


n = int(input('введите количество элементов в списке '))

min_max_diff_in_list(random_list_without_int(n))