# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

a = int(input())
b = int(input())

def Sum (a, b):
    if b == 0 :
        return a
    else:
         return Sum (a + 1, b - 1)

print(Sum (a, b))