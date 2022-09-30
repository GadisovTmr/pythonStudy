# 3. Задайте список из n чисел, заполненный
# по формуле (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input('n='))
lis =list()
result = 0
for i in range(n):
    result= round((1+1/(i+1))**(i+1))
    lis.append(result)
print(lis)
