# Напишите программу, которая на вход 
# принимает число (N), а на выходе показывает 
# все чётные числа от 1 до N

number = int(input("Введите число: "))
print(number)
for i in range(1, number+1):
    if i % 2 == 0:
        print(i, end = ' ')