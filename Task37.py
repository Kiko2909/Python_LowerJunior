# Задача 43. Решение в группах
# Дан список чисел. 
# Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, 
# которую необходимо посчитать. 

# Вводится список чисел. Все числа списка находятся на разных строках.
# Ввод: 1 2 3 2 3 
# Вывод: 2

res=0

lst = [int(input()) for i in range (int(input("Сколько элементов в списке? ")))]
print(lst)

for i in range(len(lst)) :
    if lst.count(i) > 1: # Возвращает количество элементов со значением i
        res +=1

print(res)








# def Couple (my_lst,pos,count) :
#     if len(my_lst) > pos:
#         if my_lst[pos - 1] < my_lst[pos] and my_lst [pos + 1] < list_1[pos] :
#           count += 1
#         pos += 1
#         return Couple(my_lst,pos,count)
#     return count  
  
# print(Couple(list_1,a,count))