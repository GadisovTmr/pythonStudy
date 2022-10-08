# 1. Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# stroka = input("введите цифры через пробел").split()
# def func_prov (string_va):
#     for index in string_va:
#         if not index.replace('-','').isdigit():
#             return []
#     return string_va
#
# def func_vtor (spisok):
#     arr = func_prov(spisok)
#     if arr:
#         return min(arr, key=int), max(arr, key=int)
#     else:
#         return []
#
# print(func_vtor(stroka))

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
# с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
# Уравнения и корни запишите в файл.

# from math import sqrt
#
# a = float(input('введите a '))
# b = float(input('введите b '))
# c = float(input('введите c '))
# d = b*2 - 4* a *c
# sqrd = sqrt(d)
# with open('temp.txt', 'a', encoding='utf-8') as output:
#     if d >0 and a:
#         x1 = (-b + sqrd) / (2*a)
#         x2 = (-b - sqrd)/ (2*a)
#         output.write(f'первый корень равен {x1}, второй корень равен {x2}')
#     elif d == 0:
#         x = -b / (2*a)
#         output.write(f' корень равен {x} ')
#     else:
#         output.write('корней нет')

# from math import gcd
#
# a = int(input('введите a '))
# b = int(input('введите b '))
#
# def nok (first, second):
#     return (first*second) // gcd(first ,second)
#
# print(nok(a,b))
