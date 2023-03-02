# Задача No33. Решение в группах
# Хакер Василий получил доступ к классному журналу 
# и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, 
# но наоборот: все максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1

import random

def mark_list (x) :
    mark = [random.randint(1,5) for i in range(x)]
    return mark

def remark_prog (list_1, maxi, mini) :
    for i in range(len(list_1)):
        if list_1[i] == maxi:
            list_1[i] = mini
    return list_1

num = int (input("How many marks? "))
my_list = mark_list(num)
max_elem = max(my_list)
min_elem = min(my_list)

print(my_list)
print(remark_prog(my_list, max_elem, min_elem))

