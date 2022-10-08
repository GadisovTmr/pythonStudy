# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('введите n =  '))

def mnogeteli(a):
    spisok =  []
    d = 2
    while d*d <= a:
        while a%d == 0:
            spisok.append(d)
            a = a/d
        d = d+1
    if a> 1:
        spisok.append(a)
    return spisok


print(mnogeteli(n))
