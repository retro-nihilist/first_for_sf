import numpy as np
a = np.int8(25)
print(a)
# 25

# Можно применить к самому
# названию типа данных
print(np.iinfo(np.int64))
#print (iinfo(min=-128, max=127, dtype=int8))

# Можно применить к существующему
# конкретному объекту
np.iinfo(a)
# iinfo(min=-128, max=127, dtype=int8)

b = np.uint64(124)
print(b)
# 124
print(type(b))
# <class 'numpy.uint8'>
print(np.iinfo(b))
# iinfo(min=0, max=255, dtype=uint8)

print("2**64-1 = ", 2**64-1)
print("2**128-1 = ", 2**128-1)

#Преобразуйте число -456 в беззнаковый целый тип данных с выделенной памятью 1 байт. Запишите полученное после преобразования число.

a = np.int8(-456)
print(a)

arr, step = np.linspace(-6, 21, 60, endpoint=False, retstep=True)
print(step)
