# 3. Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности в том же порядке.
import random

n = int(input('введите количество элементов в списке '))

def random_list (a):
    spisok = []
    for i in range(a):
        spisok.append(random.randint(0, 8))
    print(spisok)
    return spisok


def deletter(list):
    rlist = []
    diction = {}.fromkeys(list, 0)

    for i in list:
        diction[i] +=1

    for j in diction:
        if diction[j] == 1:
            rlist.append(j)
    print(diction)
    print(rlist)
    return rlist

print(deletter(random_list(n)))