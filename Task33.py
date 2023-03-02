# Задача 26: Напишите программу, 
# которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# A = 3; B = 5 -> 243 (35) A = 2; B = 3 -> 8

def degree (num, deg) :
       if deg > 0 :
            return degree(num * a , deg - 1)
       elif deg == 0:
            return 1
       else:
             return num

a = int(input("Введите число: "))
b = int(input("Введите степень: "))

print(degree(a,b))