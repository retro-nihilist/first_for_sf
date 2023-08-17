input_string = input('Введите последовательность чисел: ')

def find_min_max(input_string):
    list0 = input_string.split(" ") #создаём список из строк
    list1 = list(map(lambda x: x.replace(",", "."), list0))#заменяем запятые на точки
    #print("p1=",list1)
    list2=list()#создаём пустой список в которой будем заносить приведённые к числам данные
    for i in list1:
        #print(i,type(i))
        if i.isalpha() == False:#пропускаем текст обрабатываем числа
            if "." in i: num=float(i)#фиксируем число с плавоющей точкой
            else: num=int(i)#фиксируем целое число 
            list2.append(num)#добавляем число в список
    return "Minimum: "+ str(min(list2))+ "\n"+ "Maximim: "+ str(max(list2)) #возвращаем результат работы функции
            #Находим минимальное значение                      Находим максимальное значение

print(find_min_max(input_string))   

#-2,56 25,002 восемь 19,13 13 -37,5