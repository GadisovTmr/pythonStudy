import random
from random import choices

# def magic(fnum1,fnum2):
#     if fnum1<0:
#         return "error"
#     ls = random.sample(range(num1*2), num1)
#     print(ls)
#     if fnum2 in ls:
#         return "Yes"
#     else:
#         return "No"
#
# num1 = int(input('введите n1 - '))
# num2 = int(input('введите n2 - '))
# print(magic(num1,num2))

# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке
# либо сообщит, что её нет.

def from_words(count, source):
    list = []
    for i in range(count):
        temp = choices(source, k=3)
        list.append("".join(temp))
    return list

count, source = int(input('каунт= ')), input('символы ')

print(from_words(count,source))

def find_second(word, wordlist):
    if wordlist.count(word) > 1:
        first_int = wordlist.index(word)
        print(wordlist.index(word, first_int+1))
    else:
        print('-1')