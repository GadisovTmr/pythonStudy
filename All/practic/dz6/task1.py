# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
from random import sample


def get_list_forward_more(n):
     first_list = sample(range(n*2), n)
     print(first_list)
     res_list = [first_list[i] for i in range(1,len(first_list)) if first_list[i] > first_list[i-1]]
     return res_list

abc = int(input('введите длину списка '))
print(get_list_forward_more(abc))