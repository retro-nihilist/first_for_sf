def inv_sum_list(lst):

    # Выводим текущее значение lst
    #print(lst)
    # Задаём условие выхода из рекурсии
    if len(lst) == 0:
        return 0
    # Во всех других случаях возвращаем
    # сумму первого элемента списка 
    # и результат суммирования оставшихся
    return 1/lst[0] + inv_sum_list(lst[1:])


print(inv_sum_list([10, 4, 8]))
## 0.475

print(inv_sum_list([10, 1, 2, 4, 8]))
## 1.975

print(inv_sum_list([]))
## 0