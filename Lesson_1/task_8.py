# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

print("Введите размер шоколадки")

n = int(input("Введите сторону n: "))
m = int(input("Введите сторону m: "))
k = int(input("Введите сколько хотите отломить: "))

# если хотя бы одна сторона без остатка и реальное количество долек не больше чем запрашиваемое, то тру
# if (k >= n and k >= m):
if (k % n == 0 or k % m == 0) and k <= n * m:
    print("yes")
else:
    print("no")