"""Игра угадай число
Загадывает компьютер, Угадывает компьютер, Считаем эффективность
на основе анализа 1000 итераций
"""

import numpy as np
#import random
count_list=list()
import random
start = 1  # начало диапазоа чисел из которых загадывает компьютер 
end = 100  # окончание диапазона чисел из котороо загадывает компьютер
per = 1 # колличество проверок алгоритма

while per > 0:
    number = random.randint(start, end) # загадываем число
    print("Загадано число = ",number)
    count = 0
    x = (end - start)//2
    s = start
    e = end

    while True:
        count+=1
        predict_number = x

        if predict_number > number:
            print(x,"Число должно быть меньше!")
            e = x
            x = s + (x - s)//2

        elif predict_number < number:
            print(x, "Число должно быть больше!")
            s = x
            x = e - (e - x)//2
        
        else:
            print(f"Вы угадали число! Это число = {number}, за {count} попыток")
            break #конец игры выход из цикла

    per = per -1
    #print(count)
    count_list.append(count)
    #print(max(count_list)) #Использовалось для проверки эффективности алгоритма