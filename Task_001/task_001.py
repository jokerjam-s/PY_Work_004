# Вычислить число c заданной точностью d
#
# Пример:
# 
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import os
import decimal as dc

# запрос вещественного числа 
def input_float(msg: str)-> float:
    return float(input(msg))

# запрос целочисленного числа 
def input_int(msg: str)-> int:
    return int(input(msg))


## MAIN ##

os.system('cls')

num = input_float('введите число: ')
precision = input_int('введите точность (чисел после запятой): ')

num = dc.Decimal(num)


print(round(num, precision))