# Функция для выпрямления списка
def flatten(lst): 
    print ("lst",lst)
    result = []   # Создаём новый пустой список
    for elem in lst: # Создаём цикл по элементам списка
        print ("elem",elem)
        if type(elem) is list:  
            print ("элемент списка является списком")
            result += flatten(elem)  # Применяем к нему функцию выпрямления и добавляем элементы к результату
            print ("result", result)
        else: # Если элемент не является списоком,
            print("элемент не является списоком")
            result.append(elem)  # Добавляем элемент в новый список
            print ("result", result)
    
    i=0
    r=0
    for i in result:
        r += i
    print (r)
    return result

matrix = [
    [1, 1, 0],
    [4, 2, 1],
    [0, 2, 1]
]

matrix = [
    [1, 1, [5, 10, 34, [24, 1, 0]]],
    [4, [9, 8, 10], 1],
    [0, 2, 1]
]
print(flatten(matrix))