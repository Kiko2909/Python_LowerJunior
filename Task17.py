# Задача No19. 
# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, 
# K – положительное число.

# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения списка или список задан изначально.

my_list = [1, 2, 3, 4, 5]
k = int(input("Число сдвига: "))

while k > 0 :
    my_list.append(my_list[0])
    my_list.remove(my_list[0])
    k -= 1
print(my_list)