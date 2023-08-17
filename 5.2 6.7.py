def sum_list(matrix):
    def sum_list2(matrix):
        result = []   # Создаём новый пустой список
        for elem in matrix: # Создаём цикл по элементам списка
            #print ("elem",elem)
            if type(elem) is list:  
                #print ("элемент списка является списком")
                result += sum_list2(elem)
                #print ("result", result)
            else: # Если элемент не является списоком,
                #print("элемент не является списоком")
                result.append(elem)  # Добавляем элемент в новый список
                #print ("result", result)
        return result
    
    i=0
    r=0
    for i in sum_list2(matrix):
        r += i
    #print (r)

    return r




matrix = [
    [1, 1, 0],
    [4, 2, 1],
    [0, 2, 1]
]
print(sum_list(matrix))
## 12

matrix = [
    [1, 1, [1, 2, 3], 0],
    [4, 2, 1, [10, 52, 2]],
    [0, 2, 1]
]
print(sum_list(matrix))
## 82    