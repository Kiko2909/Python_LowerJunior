# Задача No39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 

# Пользователь вводит число N - количество элементов в первом массиве, 
# затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. 
# Затем элементы второго массива

element_1 = int(input("Сколько элементов в первом массиве? "))
list_1 = list()
for i in range(element_1) :
	list_1.append(int(input()))
print( list_1 )

element_2 = int(input("Сколько элементов во втором массиве? "))
list_2 = list()
for i in range(element_2) :
	list_2.append(int(input()))
print( list_2 )

my_s1, my_s2  = set(list_1), set(list_2)
print(*my_s1.difference(my_s2))