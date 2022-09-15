# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 
# Факторизацией называется разложение числа на простые множители. 
# Если у числа существует простой делитель, отличный от него самого, то он не превышает корня из числа.

import os
import math as mt

# запрос целочисленного числа 
def input_int(msg: str)-> int:
    return int(input(msg))

# поиск множителей
def get_factors(n):
    fact = []

    for i in range(2, int(mt.sqrt(n))+1):
        while n % i == 0:
            n = n / i
            fact.append(i)
    
    if(n > 1):
        fact.append(int(n))

    return fact

## MAIN ##
os.system('cls')

num = input_int('Введите число: ')
print(get_factors(num))



