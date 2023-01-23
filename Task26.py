# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input())
b = int(input())

def degree(m, n):
    if m == 1:
        return 1
    elif n == 1:
        return m
    else:
        return degree(m, n-1) * m

print(degree(a, b))
