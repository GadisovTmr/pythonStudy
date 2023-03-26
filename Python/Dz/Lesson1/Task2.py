# Монетки

# n = int(input('Кол-во монет'))
# count_zero = 0
# count_one = 0
# for i in range(n):
#     x = int(input())
#     if x == 0:
#         count_zero += 1
#     else:
#         count_one += 1
# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)

# Петя и Катя

# s = int(input('введите сумму'))
# p = int(input('введите произведение'))
#
# for i in range(s):
#     for j in range(p):
#         if s == i+j and p == i*j:
#             print(i,j)

# Степени 2

n = int(input())
i=0
while 2 ** i <= n:
    print(2 ** i)
    i += 1

