# Задача No41. Решение в группах
# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.


list_1 = [int(input()) for i in range (int(input("Сколько элементов в массиве? ")))]
print(list_1)
count = 0
a = 0
# for i in range (1, len(list_1) - 1) :
#     if list_1 [i - 1] < list_1[i] and list_1 [i + 1] < list_1[i] :
#         count += 1
# print(count)

def Numbers (my_lst,pos,count) :
    if len(my_lst)-1 > pos:
        if my_lst[pos - 1] < my_lst[pos] and my_lst [pos + 1] < list_1[pos] :
          count += 1
        pos += 1
        return Numbers(my_lst,pos,count)
    return count  
  
print(Numbers(list_1,a,count))