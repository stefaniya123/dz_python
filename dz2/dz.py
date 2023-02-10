# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# num = input("Введите число: ")
# num=abs(float(num))
# sum = 0
# for i in str(num):
#     if i != ".":
#          sum += int(i)
# print(f"Сумма цифр = {sum}")



# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n=int(input("Введите число N"))
# list=[]
# f=1
# x=1
# for i in range(1,n+1):
#     list.append(f)
#     x=x+1
#     f=f*x
# print(list)

# squares = {}
# sum=0
# n=int(input("Введите число"))
# for i in range(1,n+1):
#     squares[i] = round((1+1/i)**i,2)
#     sum=sum+squares[i]
# print(squares,"Сумма ",sum)