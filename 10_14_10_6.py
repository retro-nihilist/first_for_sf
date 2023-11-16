import numpy as np
"""numpy.zeros(shape, dtype=float, order='C', *, like=None)

Return a new array of given shape and type, filled with zeros.

Parameters:
shapeint or tuple of ints
Shape of the new array, e.g., (2, 3) or 2.

dtypedata-type, optional
The desired data-type for the array, e.g., numpy.int8. Default is numpy.float64.

order{‘C’, ‘F’}, optional, default: ‘C’
Whether to store multi-dimensional data in row-major (C-style) or column-major (Fortran-style) order in memory.

likearray_like, optional
Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as like
supports the __array_function__ protocol, the result will be defined by it. In this case, it ensures the creation
of an array object compatible with that passed in via this argument."""

def get_chess(a):
    array = np.zeros((a, a))
    #print(array)
    array[1::2, ::2] = 1     # Задаем 1 в соответствии с шахматным порядком по СТОЛБЦАМ
    #print(array)
    array[::2, 1::2] = 1     # Задаем 1 в соответствии с шахматным порядком по СТОЛБЦАМ
    #print(array)
    data_type = array.dtype

    #print("Тип данных в массиве:", data_type)

    return(array)
print(get_chess(a = 5))


