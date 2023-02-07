# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

# 0  1  1  2  3  5  8  13  21    Числа Ф
# 1  2  3  4  5  6  7  8   9     Номера

print ("Введите число: ")
a = int(input())

num1 = 0 #1
num2 = 1 #2

index = 2

while num1 < a:
    num1 += num2
    index += 1 

    if num1 == a :
        print(index)
        break

    num2 += num1 
    index += 1
    
    if num2 == a :
        print(index)
        break

if num1 > a : 
    print(-1)


