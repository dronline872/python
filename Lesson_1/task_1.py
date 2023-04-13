# Задача 2: Найдите сумму цифр трехзначного числа.
number = input("Введите трехзначное число: ")
sum = 0

for i in number:
    sum = sum + int(i)

print(f"Сумма цифр числа {number} = {sum}")