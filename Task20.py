#  Задача 16: Требуется вычислить, сколько раз встречается некоторое
#  число X в массиве A[1..N].

#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#  В последующих строках записаны N целых чисел Ai
#  Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3 -> 1

n = int(input("Сколько элементо в массиве? "))
my_lst = list()

def search(num):
    return my_lst.count(num)

for i in range (n) :
    my_lst.append(int(input()))
print(my_lst)

print ("Данное число упоминается ",search(int(input("Какое число найти? "))), " раз(-а)")


