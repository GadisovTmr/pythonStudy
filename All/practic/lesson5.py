# # 1. Создайте список из N натуральных чисел(0 до N),
# # упорядоченных по возрастанию. Среди чисел не хватает
# # одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# # Найдите это число.
#
# from random import choice
#
# def fil_list(num):
#     array = [i for i in range(num+1)]
#     array.remove(choice(array))
#     return array
#
#
#
#
# def checher(array):
#     for i in range(1, len(array)):
#         if array[i] - 1 != array[i-1]:
#             return array[i-1]
#     return -1
#
# abc = fil_list(10)
# print(abc)
#
# print(checher(abc))

# 2. Создайте список, в который попадают числа,
# описывающие возрастающую последовательность.
# Порядок элементов менять нельзя.

from random import choices
def get_list(n):
    return choices(range(n*2), k=n)

def find_list(lis):
    lsc = []
    for i in range(len(lis)):
        cur = lis[i]
        cur_lis = [cur]
        for k in range(len(lis)):
            if lis[k] > cur:
                cur_lis.append(lis[k])
                cur = lis[k]
        if len(cur_lis) > 1:
            lsc.append(cur_lis)
    return lsc


paaa = get_list((int(input('chislo '))))
print(paaa)
print(find_list(paaa))
