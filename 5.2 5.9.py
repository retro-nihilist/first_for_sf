


def fib(n):
    # Задаём условия выхода из рекурсии:
    if n==1: return 1
    if n==2: return 1
    # Во всех других случаях возвращаем
    # произведение текущего числа n и функции от n-1
    return fib(n-1)+fib(n-2)





print(fib(1))
# 1
print(fib(2))
# 1
print(fib(6))
# 8