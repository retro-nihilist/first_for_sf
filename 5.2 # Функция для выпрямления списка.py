# Функция для выпрямления списка
def flatten(lst):
    # Создаём новый пустой список
    result = []
    # Создаём цикл по элементам списка
    for elem in lst:
        # Если элемент списка является списком,
        if type(elem) is list:
            # Применяем к нему функцию выпрямления и добавляем элементы к результату
            result += flatten(elem)
        else: # Если элемент не является списоком,
            # Добавляем элемент в новый список
            result.append(elem)
    return result

matrix = [
    [1, 1, 0],
    [4, 2, 1],
    [0, 2, 1]
]

print(flatten(matrix))

matrix = [
    [1, 1, [5, 10, 34, [24, 1, 0]]],
    [4, [9, 8, 10], 1],
    [0, 2, 1]
]
print(flatten(matrix))