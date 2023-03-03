#  Задача 32: 
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4,-2,10,2,0,-9,8,10,-9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint

lst = [randint(-20,20) for i in range(20)]
print(lst)

mini = int(input("Minimum: "))
maxi = int(input("Maximum: "))
res = []

for i in range(len(lst)):
    if lst[i] > mini and lst[i] < maxi :
        res.append(i)
print(*res)