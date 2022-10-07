# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.



def decimal_to_binary(n):
    spisok =[]
    sum=0
    if n == 0:
        spisok.append(0)
        spisok
    while n>0:
        spisok.insert(0,n%2)
        n=n//2
    return spisok

n = int(input('введите число для преобразования '))
print(decimal_to_binary(n))

