# 1. Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр

n = float(input('n='))
nstr = str(n)
lenofnumbers = len(nstr)
resule = n*10**(lenofnumbers-1)
count = 0
while resule>0:
    count = count + resule%10
    resule = resule//10
print(count, resule)

