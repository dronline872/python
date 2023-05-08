# Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def factorial(i = 1, n = 1):
    if i < n:
        return i * factorial(i+1, n)
    else:
        return n

def triangular(i = 1, n = 1):
    if i < n:
        return i + triangular(i+1, n)
    else:
        return n

f = int(input("Введите число для получения факториала: "))
print(f"Факториал = {factorial(1, f)}")

t = int(input("Введите число для получения треугольного числа: "))
print(f"Треугольное число = {triangular(1, t)}")
