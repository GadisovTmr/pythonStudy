# типы данных: int, float, boolean, str, list, None, value
# print -  вывод  input -  ввод 
# арифметика  / - деление // - деление в целых числах % - остаток от деления ** - возведение в степень 
# round - округление, можно напимсать print(a:0.4)
# присваивание, например а=5 а = а+5 можно написать а +=5
#  строки   print(len(a)) - длина, text.replace('привет' , 'ПриВет'), text.islower, text.isdigit ,
#  str.count - подсчет str.count('что ищем', с какого символа, по какой символ), str.split - разбив на строки
# str.joint - объеденить
#  ФУНКЦИИ ЧЕРЕЗ def

# a= 123
# b= 2.21
# c = "hello"
# print (a,b,c)
# print (a, '-', b, '-', c)
# print ('{} - {} - {}'.format(a,b,c)) можно в фигурных указать последовательность из формата типа 1 0 2 
# print (f' {a-2} - {b}')  интерполяция, не забывать про f

# f = True
# print(f)

# list = [1,2,23, 'asd']  но лучше однотипные данные в списках 
# # print(list)
# print('Введите а')
# a = int(input())
# print('а теперь b')
# b = int(input())
# print (a, '+', b, ' = ', a+b)

# a = 123
# b = -23
# c= a+b
# print(c)

# a = 123.213123
# b = -2.2
# c= round(a+b,5)
# print(c)

# a = 1<3 and 5>2
# print(a)
# a = 'qwe'
# b = 'qwe'
# print (a==b)
# a = [1,2]
# b = [1,2]
# print(a==b)

# a = 1<3<5 можно использовать несколько неравнест
# print(a)

# a = 1>2 or 4<6
# print(a)
# a = [1,2,3] 
# # print(not 2 in a)
# # print(2 in a) типа поиска в масиве
# is_odd = not a[1] %2 
# print(is_odd)
#                               IF ELSE ELIF
# a= int(input('a='))
# b= int(input('b='))
# if a> b:
#     print(a)
# else:
#     print(b)   elif = проверка 2 и тд условия

#                           WHILE FOR 

# a = 23
# inverted_a = 0
# while a != 0:
#     inverted_a = inverted_a*10 + (a%10)
#     a //=10
# else:
#     print('наверное хватит')
# print(inverted_a)

# list = [1,2,3,4,5]
# for i in list:
#     print(i**3)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(10,20, 3):
#     print(i)

# for i in 'qwesd sd':
#     print(i)

# list.append('aasd')  - добавить aasd в конец списка
# list.remove('aasd') - удалит aasd из списка 
# del list[0] - удалит 0 элемент в списке 

# def name_ofdunct(a):
#     if a == 1:
#         return 'целое'
#     elif a == 2.3:
#         return 23
#     else:
#         return

# arg = 2
# print(name_ofdunct(arg))
# print(type(name_ofdunct(arg)))
