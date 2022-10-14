# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.

from random import sample


def list_s(count):
    str = 'абв'
    words_l = []
    for i in range(count):
        lett = sample(str, 3)
        words_l.append("".join(lett))
    return " ".join(words_l)


def delet_word(words):
    return " ".join(words.replace("абв", "").split())


result = list_s(int(input("Number")))
print(result)
print(delet_word(result))