# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# 
# Пример:
#
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#

import numpy as np
import os
import random as rnd


os.system('cls')
k = int(input('Степень числа: '))

list_koef = [rnd.randint(0, 101) for _ in range(k+1)]
print(list_koef)
print(np.poly1d(list_koef))

