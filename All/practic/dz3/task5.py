# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


def ne_feb(n):
    spisok = [0]
    f1 = 1
    f2 = 1
    spisok.append(f1)
    spisok.append(f2)
    spisok.insert(0, f1)
    spisok.insert(0, (-1 * f1))
    while n > 2:
        f1, f2 = f2, f1 + f2
        spisok.append(f2)
        if spisok[0] < 0:
            spisok.insert(0, f2)
        else:
            spisok.insert(0, (-1 * f2))
        n -= 1
    print(spisok)
    return spisok

n = int(input('Введите число'))
ne_feb(n)