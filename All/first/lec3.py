

# def f1(x):
#     return x**2
#
# # g = f1  мы можем положить функцию в переменную
#
# g = f1
#
# print(f1(2))
# print(g(2))
#
# print(type(f1))
# # print(type(g))
#
# def calc(x):
#     return x+10
#
# def calc2(x):
#     return x*10
#
# def math(op,x):
#     print(op(x))
#
# math(calc2,10)

#
# def sum(x,y):
#     return x+y

# sum=lambda x,y:x+y  вот так можно описать функцию
#
# def mylt(x,y):
#     return x*y

# def calc(op, a,b):
#     print(op(a,b))
#     # return
#
#
# calc(lambda x,y:x+y,9,23)


#                           list comprehensive

# list = []
# for i in range(1,101):
#     # if (i%2 ==0):
#         list.append(i);


#
# list=[i for i in range(1,21) if i%2 ==0]
# print(list)
#
# list=[(i,i) for i in range(1,21) if i%2 ==0]
# print(list)

# def f(x):
#     return x**3
# # list=[f(i) for i in range(1,21) if i%2 ==0]
# # print(list)
#
# list=[(i, f(i)) for i in range(1,21) if i%2 ==0]
# print(list)



# num = [1,2,3,4,5,12,123,13,14,15]
#
#
# out = []
# for e in num:
#     if not e%2:
#         out.append((e,e**2))
# print(out)

# def select(f,col):
#     return [f(x) for x in col]
#
# def where(f,col):
#     return [x for x in col if f(x)]
#
# data = '1 2 3 5 8 15 23 38'.split()
#
# res = select(int, data)
# res = where(lambda x: not x%2,res)
# res = select(lambda x:(x,x**2),res)
# print(res)


# li = [x for x in range(1,20)]
#
# li = list(map(lambda x:x+2, li))
#
# print(li)

# data = list(map(int,  input().split()))
#
# print(data)

# map может быть использован вместо придуманной нами селект

# def where(f,col):
#     return [x for x in col if f(x)]
#
# data = '1 2 3 5 8 15 23 38'.split()
#
# res = list(map(int, data))
# res = where(lambda x: not x%2,res)
# res = list(map(lambda x:(x,x**2),res))
# print(res)

# filter - вместо where

# data = [x for x in range(10)]
#
# res = list(filter(lambda x:  not x%2,data))
# print(res)
#
# data = '1 2 3 5 8 15 23 38'.split()
#
# res = list(map(int, data))
# res = list(filter(lambda x: not x%2,res))
# res = list(map(lambda x:(x,x**2),res))
# print(res)

#  ФУНКЦИЯ zip

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4,5,9,14,7]
# salaty = [111,222,333]
#
# data= list(zip(users,ids,salaty))
# print(data)

#  функция enumerate
#
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# data = list(enumerate(users))
# print(data)




lisst = [1,2,3,5,8,15,23,38]
def d(x):
    return x**2

list = [(i, d(i)) for i in (lisst) if i%2 ==0]


print(list)


