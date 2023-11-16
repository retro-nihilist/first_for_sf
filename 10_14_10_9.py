import numpy as np

def any_normal(*vectors):
    # Проверяем, что хотя бы один вектор передан
    if len(vectors) == 0:
        raise ValueError("Нет переданных векторов")

    # Преобразуем входные векторы в массивы NumPy
    vectors = [np.array(vector) for vector in vectors]

    # Проверяем, что все векторы имеют одинаковую длину
    if not all(len(vector) == len(vectors[0]) for vector in vectors):
        raise ValueError("Все векторы должны иметь одинаковую длину")

    # Проверяем пары векторов на перпендикулярность
    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            dot_product = np.dot(vectors[i], vectors[j])
            if dot_product == 0:
                return True

    return False

"""
Напишите функцию any_normal, которая принимает на вход неограниченное число векторов через запятую.
Гарантируется, что все векторы, которые передаются, одинаковой длины.

Функция возвращает True, если есть хотя бы одна пара перпендикулярных векторов. Иначе возвращает False.

Пример

vec1 = np.array([2, 1])
vec2 = np.array([-1, 2])
vec3 = np.array([3,4])
print(any_normal(vec1, vec2, vec3))
# True"""