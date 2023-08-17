def print_personal_data(**data):
    #print(data)
    data_k=sorted(data.items())
    #print(data_k)
    data = dict(data_k)
    #print(data)
    #print(len(data))
    for i in data:
        print(i,": ", data[i], sep='')
        #print(str(data.items()[i]))


print_personal_data(first_name='John', last_name='Doe', age=28, position='Python developer')
# age: 28
# first_name: John
# last_name: Doe
# position: Python developer


"""Напишите функцию print_personal_data(), которая должна принимать
 на вход неизвестное количество именованных аргументов (персональных данных)
   в любом порядке и выводить их в виде аргумент: значение в отсортированном 
   по алфавиту порядке имён аргументов.

Примеры работы функции:




print_personal_data(first_name='Jack', last_name='Smith', age=32, 
work_experience = '5 years', position='Project manager')
# age: 32
# first_name: Jack
# last_name: Smith
# position: Project manager
# work_experience: 5 years"""