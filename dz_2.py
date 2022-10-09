# Напишите программу, которая принимает 
# на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве
import math
print("Введите координаты точки a: ")
xa = int(input())
ya = int(input())
print("Введите координаты точки b: ")
xb = int(input())
yb = int(input())
result = math.sqrt((xb - xa)*(xb - xa) + (yb - ya)*(yb - ya))
print(result)