# Задача 45. Решение в группах
# Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 

# Например, 220 и 284 – дружественные числа. По данному числу k 
# выведите все пары дружественных чисел, каждое из которых не превосходит k. 

# Программа получает на вход одно натуральное число k, не превосходящее 10 в 5 степени. 
# Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами. 
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

# Ввод: 300 
# Вывод: 220 284

dictionary = {284: '220 284', 1210: '1184 1210', 2924: '2620 2924', 
              5564: '5020 5564', 6362: '6232 6362',
              10856: '10744 10856', 14595: '12285 14595', 
              18416: '17296 18416', 76084: '63020 76084',
                66992: '66928 66992', 71145: '67095 71145', 
                87633: '69615 87633', 88730: '79750 88730'}

a = int(input("Введите число:"))
print("Список дружественных чисел: ")

for key in dictionary:
    if key <= a :
        print(dictionary[key])


# k = int(input('Введите число k: '))

# sum_dict = dict()
# for i in range(1, k + 1):
#     sum_dict[i] = 1
#     for j in range(2, i):
#         if i % j == 0:
#             sum_dict[i] += j

# for i in range(1, len(sum_dict) + 1):
#     for j in range(i + 1, len(sum_dict) + 1):
#         if i == sum_dict[j] and j == sum_dict[i]:
#             print(i, j)