# Введите свое решение ниже
print_on_off = 1
import numpy as np
np.random.seed(2021)
#В simple сохраните случайное число в диапазоне от 0 до 1
simple = np.random.rand()
if print_on_off > 0: print("simple = ", simple)
#Сгенерируйте 120 чисел в диапазоне от -150 до 2021, сохраните их в переменную randoms
randoms = np.random.uniform(low=-150, high=2021, size=120)
#Получите массив из случайных целых чисел от 1 до 100 (включительно) из 3 строк и 2 столбцов. Сохраните результат в table
table = np.random.randint(low=1, high=101, size=(3, 2))
#В переменную even сохраните четные числа от 2 до 16 (включительно)
even = np.arange(2, 17, 2)
if print_on_off > 0: print("even = ", even)
"""Ожидаемый ответ:
[ 2  4  6  8 10 12 14 16]
Ваш ответ:
[12  4 12  4  8  2  4  6]"""
#Скопируйте even в переменную mix. Перемешайте числа в mix так, чтобы массив изменился
mix = np.random.permutation(even)
#Получите из even 3 числа без повторений. Сохраните их в переменную select
select =np.random.choice(even, size=3, replace=False)
#Получите переменную triplet, которая должна содержать перемешанные значения из массива select (сам select измениться не должен)
triplet = np.random.permutation(select)