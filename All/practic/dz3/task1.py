# 1.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

import random

n = int(input('введите количество элементов в списке '))


def random_list (a):
    spisok = []
    for i in range(a):
        spisok.append(random.randint(0, 10))
    print(spisok)
    return spisok

def sum_of_pare(list):
    sum=0
    a = range(len(list))
    for i in a:
        if (i % 2) == 0:
            sum = sum + list[i]
    return sum

n = int(input('введите количество элементов в списке '))
print(sum_of_pare(random_list(n)))


