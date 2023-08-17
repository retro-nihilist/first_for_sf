def even_numbers_in_matrix(matrix):
    n=0
    for i in matrix:
        for ii in i:
            if ii%2 == 0:
                n = n+1
    return n






matrix_example = [
    [1, 5, 4],
    [4, 2, -2],
    [7, 65, 88]
]
print(even_numbers_in_matrix(matrix=matrix_example))

"""Напишите функцию even_numbers_in_matrix(), которая 
получает на вход матрицу (список из списков) matrix и
 возвращает количество чётных чисел в ней.

Гарантируется, что все элементы в матрице matrix являются
 числами.

Пример работы программы:



# 5"""