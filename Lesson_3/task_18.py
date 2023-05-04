# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input("Введите количество чисел в массиве: "))
numbers = []
for i in range(n):
    numbers.append(int(input("Введите число: ")))
x = int(input("Введите число которое хотите найти: "))

temp = 0
number = 0
for num in numbers:
    diff = abs((num / x) - 1)
    if diff == 0:
        number = num
        break
    elif temp == 0 or diff < temp:
        temp = diff
        number = num
print(f"Самое близкое число {number}")
