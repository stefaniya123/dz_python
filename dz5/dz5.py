# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.


# a=int(input('Введите число А '))
# b=int(input('Введите число В '))

# def pov(a,b):
#     if b==1:
#         return a
#     while(b>1):
#         return a*pov(a,b-1)
# print(pov(a,b))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

a=int(input('Введите число А '))
b=int(input('Введите число В '))

def Sum(a,b):
    if b==1:
        return a+1
    return a+Sum(1,b-1)

print(Sum(a,b))