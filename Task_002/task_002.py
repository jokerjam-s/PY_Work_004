# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 
# Факторизацией называется разложение числа на простые множители. 
# Если у числа существует простой делитель, отличный от него самого, то он не превышает корня из числа.

import os
import math as mt
from unittest import result

# запрос целочисленного числа 
def input_int(msg: str)-> int:
    return int(input(msg))

def factoriz(n):
    result = []

    for i in range(2, mt.sqrt(float(n))):
        while(n % i == 0):
            n /= i
            result.append(i)

    return result


## MAIN ##
os.system('cls')

num = input_int('Введите число: ')
print(factoriz(num))


