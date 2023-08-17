def find_min_number(a,b,c):
#def find_min_number(x,y,z):
    x=a; y=b; z=c
    if x<y and x<z: return x
    if y<x and y<z: return y
    if z<x and z<y: return z
print(find_min_number(a = -1, b = 0, c = 10))
#print(find_min_number(10.9, 12.2, 18.4))


"""
Напишите функцию find_min_number(), которая принимает на вход три числа (a, b, c) 
и возвращает наименьшее из них.

Для решения задачи не используйте встроенную функцию min() — реализуйте алгоритм 
самостоятельно, воспользовавшись условными операторами.

Примеры работы функции:


print(find_min_number(130, 122, 19))
# 19
print(find_min_number(10.9, 12.2, 18.4))
# 10.9
"""