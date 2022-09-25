# 1 напишете прогу, которая проверяет выходной ли это день

print('Введите день')
dayofweek = int(input())
if dayofweek == 6 or dayofweek == 7:
    print('это выходной день') 
elif dayofweek >= 1 and dayofweek < 6:
    print('это будний день')
else:
    print('введен не день недели ')

