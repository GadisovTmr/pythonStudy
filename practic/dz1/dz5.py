# Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние между ними в 2D пространстве.

x1= int(input('Введите x1  '))
y1= int(input('введите y1 '))
x2= int(input('Введите x2  '))
y2= int(input('введите y2  '))
distnce = ((x2-x1)**2 + (y2-y1)**2)**0.5
print('расстрояние равно ', round(distnce, 3))
