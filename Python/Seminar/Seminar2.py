# задача 9 factorial

# n = int(input(print('Введите n')))
# res=1
# while n > 1:
#     res=res*n
#     n -= 1
#
# print(res)

# Задача 11 Фибоначи
n = int(input(print('Введите n')))
first = 0
second = 1

for i in range(n):
    print(first)
    first, second = second, first
    second+=first