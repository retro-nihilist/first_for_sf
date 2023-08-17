o=(0, 4, 6, 8, 8, 9)
holes = 0
def holes_count(x):
    x_lst = list(str(x))
    x_lst=[int(x) for x in x_lst]
    #holes = 0
    #print (x_lst)
    for i in o:
        #z = x_lst.count(i)
        holes = holes + x_lst.count(i)
            #print(holes)
            
    return holes    

    

print(holes_count(8))
# 2
print(holes_count(146))
# 2
print(holes_count(84628))
# 6
"""Напишите функцию holes_count(), которая принимает на
 вход число number, подсчитывает общее количество отверстий в заданном числе и возвращает результат.

Условимся, что цифрами с отверстиями будем считать 
0, 4, 6, 8 и 9. Причём в цифре 8 отверстий два, а в 
остальных — по одному.

Обратите внимание, что функция должна возвращать 
суммарное количество отверстий по всем цифрам в числе.

Примеры работы программы:


"""