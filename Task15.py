# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

#  10 -> 1 2 4 8

num = int(input("Введите число: "))
a = 1
while a < num :
    print(a)
    a *= 2