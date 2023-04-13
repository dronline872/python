# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

ticket = input("Введите номер билета: ")
leftNumber = ticket[:3]
leftSum = 0
for l in leftNumber:
    leftSum = leftSum + int(l)

rightNumber = ticket[-3:]
rightSum = 0
for r in rightNumber:
    rightSum = rightSum + int(r) 

if leftSum == rightSum:
    print("yes")
else:
    print("no")