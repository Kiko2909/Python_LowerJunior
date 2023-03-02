# Задача 31. Решение в группах
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
# Input: 7 Output: 21
# Задание необходимо решать через рекурсию

def Fibonacci(a) :
    if a == 0 :
        return 0 
    elif a == 1 or a == 2 :
        return 1
    else :
        return Fibonacci(a - 1) + Fibonacci(a - 2)
    
count = int(input("Введите порядковый номер: "))
print("Данное число --> ", Fibonacci(count))
