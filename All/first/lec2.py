# файлы  a - открыте для довбавлени данных  r -  открытиые для чтения данных, w - отрытие для записи
# imoprt NAMEOFFILE as NameincurrentPythonFile
#  если ставим звездочку перед аргументотм в функции то будет неограниченное кол-во аргументов

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# # data.writelines(colors)
#
# data.write('Line 4\n')
# data.write('Line 5 \n')
# data.close()

# with open('file.txt', 'a') as data:
#     data.write('line\n')
#     data.write('line 2\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
# exit()

# import lec
# print(lec.name_ofdunct(1))

# import lec as mine
# print(mine.name_ofdunct(1))

#
# def new_string (symbol, count):
#     return symbol*count
#
# print(new_string('!',5))

# def new_string (symbol, count = 3):
#     return symbol*count
#
# print(new_string('!'))
# print(new_string(4))

# def concate(*params):
#     res: str = ""
#     for item in params:
#         res+= item
#     return res
# print(concate('a', 's','w'))
# print(concate('a','1'))

# def concate(*params):
#     res = 0
#     for item in params:
#         res+= item
#     return res
# print(concate(1,3,5))

#                               РЕКУРСИЯ

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib((n-2))
# print(fib(10))
# list =[]
# for e in range(1,10):
#     list.append((fib(e)))
# print(list)

                        # Кортежи

# a, b = 3, 4  - двойное присваивание
# a = (3,4,6,8)
# print(a)
# print(a[0])
# print(a[-1])  -1 - последний элемент  в списках, строках и кортежа=
# for item in a:
#     print(item)

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b{}'.format(red,green,blue))

# ?                         Словарь - неупорядоченная коллекция объектов с доступом по ключу

# dictionary = {}
# dictionary = \
#     {
#         'up': 'вверх',
#         'left': 'влево'
#     }
# print(dictionary)
# print(dictionary['left'])

# for k in dictionary.keys():
#     print(k)
# for k in dictionary.values():
#     print(k)

#                                       Множества
#
# colors = {'red', 'green','blue'}
# # print(colors)
# # print(type(colors))
# colors.add('gray')
# print(colors)
# colors.remove('red')
# print(colors)
# # colors.discard('red') - удалит, а если его нетт, то ничего, при ремуве будет ошибка если нет элемента
# # colors.clear() - очистит множество

# a = {1,2,3,5,6}
# b = {2,5,8,13,21}
# c = a.copy()  - копировать множество
# u = a.union(b) - объединить множетсва
# i = a.intersection((b)) - показать пересечения множетсв
# difa = a.difference(b) - покзать разницу множеств
#
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# s = frozenset(a) - создает замороженное (неизеняемое) множетсво

#               снова списки

# list1 = [1,2,3,4,5]
# list2 = list1
# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)
# print()
# list1[0] = 123
# list2[1] = 333
# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)

# list1 = [1,2,3,4,5]
# print(len(list1))
# # list1.pop()   - удалыет последний эллемент списка
# # print(list1)
# # print(len(list1))
# # list1.pop(2)  - удалит элемент под 2 индексом
# print(list1)
# list1.insert(2,123)   - добавит 123 на место под индексом 2
# print(list1)
# list1.append(444) - добавит 444 в конец