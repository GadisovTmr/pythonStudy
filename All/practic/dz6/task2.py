# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.


n = int(input('введите n '))
def del_twenty_one (n):
    list=[i for i in range(21,n+1) if  i%20 == 0 or i%21 ==0]
    return list

print(del_twenty_one(n))
