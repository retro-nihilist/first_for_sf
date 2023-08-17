input_string1 = input
input_string2 = input('Введите 2-ую последовательность идентификаторов: ')

input_list0 = list()
def pure_intersection (p):#функция сравнения.
    def chek(pp):#проверка введённых данных на корректность
        global input_list0        
        try:
            temp_list_lmd = lambda p: set(p.split(", "))#строку в смисок убираем повторения, преобразуя в множество 
            input_list0.append(list(map(int, temp_list_lmd(pp))))#создаём список с введёнными данными
            #print("p1=",input_list0)
            if len(input_list0)>1:#проверяем свормировался ли многоуровневый список для анализа
                #print("p2=",input_list0)
                def original_n(list0): return list(filter(lambda x: x in list0[1], list0[0]))#функции сравнения списков и вывод
                print(original_n(input_list0))#инициация функции сравнения списков
        except ValueError:
            # повторно запрашиваем / создаём строку для комментария к вводу / вызываем функцию
            pure_intersection(input("Некорректный ввод"+ "\n"+ 'Введите '+ str(len(input_list0)+1)+ '-ую последовательность идентификаторов: '))
    chek(p) # инициирование проверки на коректность

pure_intersection(input_string1)
pure_intersection(input_string2)
