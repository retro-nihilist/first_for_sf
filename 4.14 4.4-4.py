"""Задание 4.4
В переменных center, south и north хранятся списки из перечней купленных позиций в трёх торговых точках,
 расположенных в разных районах города.
Вначале избавьтесь от излишней вложенности: в каждой переменной (center, south, north) должен храниться
 объединённый список купленных товаров без разбиения по чекам.
Пример: [['Milk', 'Bread'], ['Meat']] -> ['Milk', 'Bread', 'Meat']
После этого определите, в каком магазине было куплено больше всего товаров.
""" 
center = [['Meat', 'Beer', 'Soap', 'Beer', 'Cheese', 'Cola', 'Milk', 'Soap', 'Cola', 'Meat', 'Bread', 'Chocolate', 'Chips'], ['Soap', 'Beer', 'Chips', 'Bread', 'Beer', 'Beer', 'Beer', 'Cheese', 'Cheese', 'Beer', 'Chips', 'Chocolate', 'Chips', 'Cheese', 'Bread', 'Cola', 'Cola', 'Beer'], ['Cola', 'Soap', 'Bread', 'Milk', 'Beer', 'Meat', 'Bread', 'Bread'], ['Ketchup', 'Beer', 'Ketchup', 'Chocolate', 'Milk', 'Milk', 'Bread', 'Beer'], ['Beer', 'Beer', 'Meat', 'Ketchup', 'Soap', 'Bread', 'Cola', 'Beer'], ['Meat', 'Bread', 'Milk', 'Cheese', 'Soap', 'Beer', 'Milk', 'Cheese', 'Cola', 'Beer', 'Chips', 'Bread', 'Ketchup', 'Chocolate', 'Bread', 'Milk'], ['Yoghurt'], ['Beer', 'Milk', 'Chips', 'Soap', 'Chips', 'Milk', 'Beer', 'Chips', 'Bread', 'Meat', 'Milk'], ['Yoghurt', 'Beer', 'Cola', 'Cola', 'Beer', 'Soap', 'Cheese', 'Soap', 'Bread', 'Cola', 'Yoghurt', 'Ketchup', 'Beer', 'Milk'], ['Milk', 'Cola', 'Bread', 'Cola', 'Bread', 'Beer', 'Beer', 'Beer'], ['Yoghurt', 'Cola'], ['Bread', 'Yoghurt', 'Chips']]
north = [['Milk', 'Milk', 'Beer'], ['Chocolate', 'Bread', 'Cola', 'Cola', 'Cola', 'Yoghurt', 'Soap', 'Beer', 'Chips', 'Milk'], ['Soap', 'Soap', 'Cola', 'Cola', 'Chips'], ['Milk', 'Beer', 'Meat', 'Ketchup', 'Cola', 'Cola', 'Chips', 'Chips', 'Cola', 'Cola'], ['Beer', 'Bread', 'Bread', 'Beer', 'Beer', 'Beer', 'Bread', 'Cheese'], ['Yoghurt', 'Beer', 'Chips', 'Milk', 'Soap', 'Cola', 'Cola', 'Cola', 'Beer', 'Cola', 'Cola', 'Cola', 'Beer', 'Ketchup', 'Beer', 'Beer', 'Beer', 'Soap'], ['Milk', 'Cola', 'Cola', 'Beer', 'Beer', 'Bread', 'Bread', 'Soap', 'Cola', 'Cola', 'Beer', 'Meat', 'Bread', 'Chips'], ['Beer', 'Beer', 'Beer', 'Chips', 'Milk', 'Cola', 'Chocolate', 'Beer', 'Chocolate', 'Beer', 'Beer', 'Cola', 'Meat', 'Yoghurt', 'Beer'], ['Bread'], ['Chocolate', 'Beer', 'Meat', 'Yoghurt'], ['Cola', 'Beer', 'Beer', 'Beer', 'Chocolate', 'Beer', 'Soap', 'Beer', 'Chips', 'Soap', 'Chocolate', 'Bread', 'Chips', 'Cola', 'Bread', 'Beer', 'Cola', 'Bread'], ['Chips', 'Cola', 'Beer', 'Chips', 'Cola', 'Cola']]
south = [['Cola', 'Meat', 'Cheese', 'Yoghurt', 'Beer', 'Milk', 'Milk', 'Meat', 'Cola', 'Cola', 'Cheese', 'Beer', 'Yoghurt', 'Beer', 'Bread', 'Bread', 'Milk', 'Cheese', 'Chocolate'], ['Soap', 'Milk', 'Cola'], ['Milk', 'Bread', 'Yoghurt', 'Meat', 'Meat'], ['Bread', 'Milk', 'Beer'], ['Beer'], ['Chocolate', 'Meat', 'Chocolate', 'Cola', 'Cola', 'Cola', 'Cola', 'Yoghurt', 'Bread', 'Meat', 'Soap', 'Soap', 'Milk', 'Milk', 'Cola'], ['Beer', 'Beer', 'Meat', 'Chips', 'Bread', 'Bread', 'Bread', 'Bread', 'Milk', 'Cola', 'Chocolate', 'Bread', 'Beer', 'Chips', 'Bread', 'Bread', 'Yoghurt'], ['Chips', 'Milk', 'Soap'], ['Meat', 'Beer', 'Milk', 'Chocolate', 'Bread', 'Yoghurt'], ['Chips', 'Meat', 'Chocolate', 'Bread', 'Cola', 'Cola', 'Chocolate', 'Meat', 'Yoghurt', 'Milk'], ['Bread', 'Soap', 'Bread', 'Meat', 'Beer', 'Yoghurt', 'Milk', 'Cola', 'Bread', 'Ketchup'], ['Meat', 'Milk'], ['Meat', 'Beer', 'Yoghurt'], ['Cola', 'Bread', 'Cola', 'Chocolate', 'Chips', 'Meat', 'Cheese'], ['Milk', 'Milk', 'Cheese', 'Meat']]

#https://dev-gang.ru/article/python-poluczit-koliczestvo-elementov-v-spiske-7xoe1p0fd7/
#-----------------------------------------------------------------------------------
def get_all_elements_in_list_of_lists(list):
    count = 0
    for element in list:
        count += len(element)
    return count
#print("center: ", get_all_elements_in_list_of_lists(center)) 
#print("north: ", get_all_elements_in_list_of_lists(north)) 
#print("south: ", get_all_elements_in_list_of_lists(south)) 
#-----------------------------------------------------------------------------------

from collections import deque
from collections import Counter # Импортируем объект Counter из модуля collections
list_deque = deque([])
dict_0 = {"center": center, "north": north, "south": south}

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
for i in list(dict_0):
    #print("i = ", i)
    summ_ii = 0
    for ii in dict_0[i]:
        #print("ii = ", ii)
        summ_ii = summ_ii + len(ii)
        #print(summ_ii)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def list_iter_0(dict_00):
    list_dict = list(dict_00)
    #print(list_dict)
    global dict_000
    dict_000 = dict()
    for i in list_dict:

        for ii in dict_00[i]:
            #print("i = ", i)
            #print("ii = ", ii)

            if all(type(x) is str for x in ii):
                #print("добавляем в список", ii)
                list_deque.extend(ii) #добавляем строку в стек
                #print("list_deque = ", list_deque)
            else:
                #print("i является списком")
                global list_i1
                list_i1 = i
                #print("вызов рекурсии", "i = ", i)
                list_iter(i)
                return list_deque
            
            #list_iter(ii)

        dict_000[i]=list(list_deque)
        #print("dict_000 = ", dict_000)
        list_deque.clear()
    #print("dict_000 = ", dict_000)

    dict_co_ter = dict()
    dict_04 = dict()
    for i in list_dict:
        dict_04[i] = len(dict_000[i])
    for i in list_dict:
        dict_co_ter[i] = Counter(list(dict_000[i]))
    #print("dict_000 = ", dict_000)
    
    #print("цикл поиска минимального значения")
    #dict_co_ter_min = dict()
    #for i in list_dict:
        #print("i = ", i)
        #https://ru.stackoverflow.com/questions/751243/%D0%9D%D0%B0%D0%B9%D1%82%D0%B8-%D0%BC%D0%B8%D0%BD%D0%B8%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B8%D0%B7-%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8F-%D1%83%D0%BF%D0%BE%D1%80%D1%8F%D0%B4%D0%BE%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5-%D0%BF%D0%BE-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8E-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D0%B0
        #print("значение = ", min(dict_co_ter[i].values()))
        #print("ключ = ", min(dict_co_ter[i], key=lambda unit: dict_co_ter[i][unit]))

    #print("dict_04 = ", dict_04)
    #print("dict_co_ter = ", dict_co_ter)
    #print(dict_000)
    #print("Выберите товар, который в магазине center покупали чаще, чем в магазине north:")
    counter_dict = dict()
    for i in list_dict:
        counter_dict[i] = Counter(dict_000[i])
    #print (counter_dict)


    
    """
    subtract_dict = dict()
    subtract_dict = counter_dict["center"]
    #print("subtract_dict (center) = ", subtract_dict)
    #print("counter_dict[north] = ", counter_dict["north"])
    #print("counter_dict[center] 1 = ", counter_dict["center"])
    subtract_dict.subtract(counter_dict["north"])
    #print("counter_dict[center] 2 = ", counter_dict["center"])
    print("subtract_dict = ", subtract_dict)


    del_dict = dict()
    print("counter_dict[center] = ", counter_dict["center"])
    print("counter_dict[north] = ", counter_dict["north"])
    del_dict = counter_dict["north"] - counter_dict["center"]
    print("del_dict = ", del_dict)
"""
    sum_dict = dict()
    sum_dict_2 = dict()
    sum_dict_3 = Counter()
    for i in list_dict:
        sum_dict_3 = sum_dict_3 + counter_dict[i]
        print("counter_dict[i] = ", counter_dict[i])
        sum_list = list(list_dict)
        sum_list.remove(i)
        #print(sum_list)
        sum_dict[i] = counter_dict[sum_list[0]] + counter_dict[sum_list[1]]
        sum_dict_2[i] = counter_dict[i] - sum_dict[i]
    print("sum_dict_3 = ", sum_dict_3)

list_iter_0(dict_0)






# В скобках передаём список при создании deque,
# чтобы сразу добавить все его элементы в очередь
shop = deque([1, 2, 3, 4, 5])
print(shop)
# deque([1, 2, 3, 4, 5])
shop.extend([11, 12, 13, 14, 15, 16, 17])
print(shop)
# deque([1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 16, 17])
#Если вдруг у турфирмы имеется договорённость с магазином, что клиенты турфирмы обслуживаются вне очереди, добавим их в начало той же очереди с помощью extendleft:

shop = deque([1, 2, 3, 4, 5])
print(shop)
# deque([1, 2, 3, 4, 5])
shop.extendleft([11, 12, 13, 14, 15, 16, 17])
print(shop)
# deque([17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5])

#Нужно использовать способ добавления сразу нескольких элементов
"""shop = deque([1, 2, 3, 4, 5])
print(shop)
# deque([1, 2, 3, 4, 5])
shop.extendleft([11, 12, 13, 14, 15, 16, 17])
print(shop)
# deque([17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5])
"""
