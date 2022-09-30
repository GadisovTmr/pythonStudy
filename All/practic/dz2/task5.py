# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
import random

n = int(input('n='))
list1 = list()
list2 = list()
count = 0
list1.append(count)
randomizer = 0
for i in range(n-1):
    count = count +1
    list1.append(count)
print(list1)


for i in range(n):
    randomizer = list1[random.randint(0,n-1-i)]
    list2.append(randomizer)
    list1.remove(randomizer)

print(list2)

