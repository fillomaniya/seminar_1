# Напишите программу, которая по заданному номеру 
# четверти, показывает диапазон возможных координат 
# точек в этой четверти (x и y)

number = int(input("Введите число четверти от 1 до 4: "))
if number < 1 or number > 4:
    print("Вы ввели неверное число")
elif number == 1:
    print("x > 0, y > 0")
elif number == 2:
    print("x < 0, y > 0")
elif number == 3:
    print("x < 0, y < 0")
elif number == 4:
    print("x > 0, y < 0")