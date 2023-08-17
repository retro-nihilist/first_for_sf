
def combination(n, k):

    def factorial(n):
        # Задаём условия выхода из рекурсии:
        if n==0: return 1
        if n==1: return 1
        # Во всех других случаях возвращаем
        # произведение текущего числа n и функции от n-1
        return factorial(n-1)*n
    
    return (factorial(n)/(factorial(n-k)*factorial(k)))

print(combination(n=10, k=5))
## 252.0
print(combination(n=12, k=3))
## 220.0
print(combination(n=1, k=1))
## 1.0
print(combination(n=0, k=0))
## 1.0