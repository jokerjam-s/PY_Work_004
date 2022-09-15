# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


# запись многочлена представм в виде строки коэфициентов, 
# разделенных пробелами 
#   например:
#       '5 2 9 0 1' = 5x^4 + 2x^3 + 9x^2 + 1
# два многочлена зипишем в файлах file_1.txt и file_2.txt
# 
#

import numpy as np
import os

## MAIN ## 

os.system('cls')
with open('file_1.txt', 'r') as data:
    str_pol_1 = data.readline()

with open('file_2.txt', 'r') as data:
    str_pol_2 = data.readline()

poly_1 = np.poly1d([int(_) for _ in str_pol_1.split(' ')])
poly_2 = np.poly1d([int(_) for _ in str_pol_2.split(' ')])

print(f'{poly_1}\n')
print(f'{poly_2}\n')
print(f'{np.polyadd(poly_1, poly_2)}')



