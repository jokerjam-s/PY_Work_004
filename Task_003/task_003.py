# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

import random as rnd
import os

os.system('cls')

list_num = [rnd.randint(0, 10) for _ in range(int(input('Кол-во чисел: ')))]

dct = {}
for i in set(list_num):
    dct[i] = 0

for i in list_num:
    dct[i] = dct[i]+1

list_res = []
for i in dct.keys():
    if dct[i] == 1:
        list_res.append(i)

print(list_num) 
print(list_res)

