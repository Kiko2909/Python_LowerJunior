# Задача 2: Найдите сумму цифр трехзначного числа.
# Примеры:
# 123 -> 6 (1 + 2 + 3) 
# 100 -> 1 (1 + 0 + 0)

print ("Введите трёхначное число: ")
a = int(input())

print("Сумма цифр равна --> ", (a//100 + a % 10 + a // 10 % 10 ))

# Для положительного числа любой длины :

# a = int (input ("Введите число: "))
# b = a
# summary = 0

# while a >= 1 :
#     x = a%10
#     summary += x
#     a //= 10

# print(b, "-->", summary)