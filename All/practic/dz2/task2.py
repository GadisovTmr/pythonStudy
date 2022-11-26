# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

n = int(input('введите n'))
lis = list()
result = 1;
for i in range(n):
    result = result * (i + 1)
    lis.append(result)
print(lis)


