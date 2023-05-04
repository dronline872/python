# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов 1 множества: "))
m = int(input("Введите количество элементов 2 множества: "))

list_1 = set()
for i in range(n):
    num = int(input("Введите число: "))
    list_1.add(num)

list_2 = set()
for i in range(m):
    num = int(input("Введите число: "))
    list_2.add(num)
result = list_1.intersection(list_2)
print(*result, sep=', ')