n = input('Введите число: ')
def decompose_factorial(fac):

    def factorial(n):# находим факториал
        return 1 if n == 1 or n == 0 else n * factorial(n-1)

    def Factor(n):# Находим множетели
        Ans = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                Ans.append(d)
                n //= d
            else: d += 1
        if n > 1: Ans.append(n)
        return Ans
    
    list_fac = Factor(factorial(int(fac))) #создаём исходные данные для вывода
    len_list_fac = len(list_fac) # определяем длинну списка с множетелями
    
    temp_str = str(str(fac)+"! = ") #строка для итогового вывода
    itr = 1#счётчик повторяющихся множетелей
    for i in range(len_list_fac):#перебираем список множетелей по индексам

        def output_str(x, y=0):# функция для формирования строки
            
            def end_str_contr(): # определяем строку следующую за множетелем
                return " * " if i+1 < len_list_fac else ""
            
            if y > 0: return temp_str + str(x) + "^" + str(y) + end_str_contr() 
            else: return temp_str + str(x) + end_str_contr()

        if  (i+1 < len_list_fac) and list_fac[i] == list_fac[i+1]: itr = itr+1 #поиск повторяющихся множетелей 
        else:
            if itr>1:#добавляем строку состоящую из нескольких множетелей в степени
                temp_str = output_str(list_fac[i], itr)
                itr = 1
            else: temp_str = output_str(list_fac[i]) #добавляем ОДИН множитель

    return temp_str

print(decompose_factorial(n))

#25! = 2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23