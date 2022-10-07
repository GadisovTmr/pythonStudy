# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random



def random_list (a):
    spisok = []
    for i in range(a):
        spisok.append(random.randint(0, 10))
    print(spisok)
    return spisok


def proizvod_of_pares_in_list(list):
    spisok_res = []
    a = len(list)
    b = range(len(list))
    for i in range(a):
        spisok_res.append(list[i] * list[-i - 1])

    if (a % 2) == 0:
        a = a // 2
        for i in range(a):
            spisok_res.pop()
    else:
        a = (a // 2) + 1
        for i in range(a):
            spisok_res.pop()

    return spisok_res

n = int(input('введите количество элементов в списке '))
print(proizvod_of_pares_in_list(random_list(n)))
