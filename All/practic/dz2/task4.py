# 4. Напишите программу, которая принимает на вход 2 числа. Задайте
# список из N элементов, заполненных числами из
# промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).


pos_1 = int(input('позиция 1= '))
pos_2 = int(input('позиция 2= '))
n = int(input('n='))
nob = n * (-1)
lis = list()
result = int
lis.append(nob)
while nob != n:
    nob = nob + 1
    lis.append(nob)
print(lis)
result = lis[pos_1 - 1] * lis[pos_2 - 1]
print(result)
