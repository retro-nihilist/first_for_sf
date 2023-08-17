def get_total_score(data):
    #print(len(data))
    data_list=[]
    for i in data: data_list.append(list(i))
    #print(data_list,"---------")
    list(map(lambda x: x.append(x[1]+x[2]+x[3]), data_list))
    data_t=[]
    for i in data_list: data_t.append(tuple(i))
    return sorted(data_t, key=lambda student: student[4])
    #return sorted(data_t)
        
        #print(list(map(lambda x: x.append(x[1]+x[2]+x[3]), ii)))
    #print(data_t,"---------")
    #print(data)
    #lambda x: x[1]+x[2]+x[3]
    #data_list = lambda y: list(y)
    data2 = [0, 0, 0, 0, 0]

    #Print(list(map(lambda x, y: y.append(x[1]+x[2]+x[3]), data, map(lambda y: list(y), data))))
    #z = list(map(lambda x: x.append(x[1]+x[2]+x[3]), map(data_list, data)))



data = [
('Amanda', 37, 78, 67),
('Patricia', 78, 93, 68),
('Marcos', 79, 67, 89),
('Dmitry', 67, 68, 100),
('Andrey', 100, 78, 76),
('Victoria', 93, 69, 96),
]

print(get_total_score(data))
# [('Amanda', 37, 78, 67, 182), ('Marcos', 79, 67, 89, 235), ('Dmitry', 67, 68, 100, 235), 
#('Patricia', 78, 93, 68, 239), ('Andrey', 100, 78, 76, 254), ('Victoria', 93, 69, 96, 258)]
""
"""Представьте, что вы работаете аналитиком в Рособрнадзоре и анализируете данные о сдаче ЕГЭ школьниками.

В вашем распоряжении есть список кортежей data. Каждый кортеж в нём состоит из четырёх элементов:

имя человека,
балл за экзамен по русскому языку,
балл за экзамен по математике,
балл за экзамен по информатике.
Напишите функцию get_total_score(), которая принимает на вход список data, добавляет в каждый кортеж 
новый элемент — общий балл по всем трём экзаменам, сортирует данные по общему баллу и возвращает 
полученный результат.

Пример работы программы:


data = [
    ('Amanda', 37, 78, 67),
    ('Patricia', 78, 93, 68),
    ('Marcos', 79, 67, 89),
    ('Dmitry', 67, 68, 100),
    ('Andrey', 100, 78, 76),
    ('Victoria', 93, 69, 96),
]

print(get_total_score(data))
# [('Amanda', 37, 78, 67, 182), ('Marcos', 79, 67, 89, 235), ('Dmitry', 67, 68, 100, 235), 
('Patricia', 78, 93, 68, 239), ('Andrey', 100, 78, 76, 254), ('Victoria', 93, 69, 96, 258)]
В процессе решения постарайтесь воспользоваться встроенной функцией map(), а также lambda-функциями.
"""
"""
"""