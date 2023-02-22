# Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6 -> 5

n = int(input("Сколько элементо в массиве? "))
my_lst = list()

def search(num):
    count = abs(num - my_lst[0])
    res = my_lst[0]
    if num in my_lst :
        return num
    else :
        for i in range(len(my_lst)):
            if abs(num - my_lst[i]) < count :
                res = my_lst[i]
                count = num - my_lst[i]
        return res



for i in range (n) :
    my_lst.append(int(input()))
print(my_lst)

print ("Ближайшее число: ",search(int(input("Какое число найти? "))))
