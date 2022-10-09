# Принимаем число и выводим его квадрат
# print('Введите число: ')
# a = int(input())
# a *= a
# print(a)

# либо:
# number = 5
# print(number * number)
# print(number ** 2)
# print(f"{number} * {number} = {number**2}")

# либо:
# number = input()
# number = int(number)
# number *= number

# либо:
# a = 5
# a **= 2
# print(a)

# ____________________________________
# Принимаем два числа и проверяем, является ли
# одно число квадратом другого

# print("Введите число A: ")
# a = int(input())
# print("Введите число B: ")
# b = int(input())
# if a * a == b or a == b * b:
#     print("Является")
# else:
#     print("Не является")
# ____________________________________

# организуйте последовательный ввод чисел до момента 
# ввода числа 0. Подсчитайте среди введенных чисел те, 
# которые кратны трем

# print("Вводите числа: ")
# number = None
# count = 0
# while number != 0:
#     number = int(input())
#     if number % 3 == 0 and number != 0:
#         count += 1
# print("Ввод окончен")
# print("Количество чисел, кратных трем, равно", count)
#______________________________________________________

# Напишите программу, которая будет на вход
# принимать число N и выводить числа от -N до N

# N = int(input("Введите число N: "))
# n = range (-N, N+1)
# print(*n)

# либо через цикл 

# import math

# N = float(input("Введите число N: "))
# N = abs(N) это возвездение числа в модуль 
# для показателя абсолютного числа
# x = math.floor(N)
# for i in range (-x, x+1):
#     print(i, end = ' ')
#__________________________

# Напишите программу, которая будет принимать на вход
# дробь и показывать первую цифру дробной части числа

# метод решения через поиск в строке

# number = input("Введите число: ")
# print(number[number.find('.') + 1] if number.find('.') > 0 else -1)

#__________________________

# Напишите программу, которая находит наибольшее
# и наименьшее число из списка значений

# numbers = [int(el) for el in input().split()]
# max_el = min_el = numbers[0]
# for number in numbers:
#     if number > max_el:
#         max_el = number
#     elif number < max_el:
#         min_el = number
# print(f'max = {max_el}')
# print(f'min = {min_el}')

# вариант через готовые операторы:

numbers = [int(el) for el in input().split()]
print(f'max = {max(numbers)}')
print(f'min = {min(numbers)}')

