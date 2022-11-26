# 5. ** Реализуйте алгоритм перемешивания списка.
import random

n = int(input('n='))
list_1 = list()
list_2 = list()
count = 0
list_1.append(count)
randomizer = 0
for i in range(n-1):
    count = count +1
    list_1.append(count)
print(list_1)


for i in range(n):
    randomizer = list_1[random.randint(0,n-1-i)]
    list_2.append(randomizer)
    list_1.remove(randomizer)

print(list_2)

