# import random
# n = int(input(' введите N '))
# lst = list()
# for i in range(n):
#     lst.append(random.randint(-10,10))
#
# print(lst)
#
# n = int(input('Введите N '))
# lst = []
# for i in range(n):
#     lst.append(3 * i + 1)
# print(lst)


# s1 = input('первый')
# s2 = input('второй')
# count = 0
# for i in range (len(s1) - (len(s2) - 1)):
#     if s2 == s1[i:i+len(s2)]:
#         count += 1
#
# print(count)

def random_list (a):
    lst = []
    for i in range(a):
        lst.append(i)
    print(lst)

random_list(5)

