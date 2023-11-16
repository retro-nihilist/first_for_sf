import numpy as np
mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
        -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
        29810.], dtype=np.float32)

"""Получите булевый массив nans_index с информацией о np.nan в массиве mystery:
True - значение пропущено, False - значение не пропущено
"""
nans_index = np.isnan(mystery)
#print(nans_index)

"""В переменную n_nan сохраните число пропущенных значений"""
# Подсчет количества искомых элементов
n_nan = np.count_nonzero(nans_index)
#print(n_nan)  # Выводит: 5

"""Скопируйте массив mystery в массив mystery_new. Заполните пропущенные значения в массиве mystery_new нулями"""
mystery_new = np.array(mystery)
mystery_new[np.isnan(mystery_new)] = 0
#print(mystery)
#print(mystery_new)

"""
Поменяйте тип данных в массиве mystery на int32 и сохраните в переменную mystery_int"""
mystery_int = mystery.astype(np.int32)

"""
Отсортируйте значения в массиве по возрастанию и сохраните результат в переменную array"""
array = np.sort(mystery)
#print(array )
"""
Сохраните в массив table двухмерный массив, полученный из массива array. 
В нём должно быть 5 строк и 3 столбца. Причём порядок заполнения должен быть по столбцам!"""

table = np.array(array)
table.shape = (3, 5)
#print(table)
table = table.transpose()
#print(table)

col = table[:, 1]
#print(col)