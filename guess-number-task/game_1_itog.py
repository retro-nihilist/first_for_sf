"""Игра угадай число
Загадываем мы угадывает компьютер
"""

start = 1  # начало диапазоа чисел из которых загадывает компьютер 
end = 100  # окончание диапазона чисел из котороо загадывает компьютер

#создаём строку предлагающую загадать число
input_str = "Pfuflfqnt число от " + str(start) + " до " + str(end) +": "

#запрашиваем число
number = int(input(input_str))

#number = random.randint(start, end) # загадываем число
#print("number = ",number)
count = 0            # переменная для фиксация количества попыток
x = (end - start)//2 # создаём первое число для сравнения
s = start            # фиксируем нижнюю границу
e = end              # фиксируем верхнюю границу

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