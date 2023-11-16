import numpy as np

def min_max_dist(*vectors):
    # Проверяем, что хотя бы один вектор передан
    if len(vectors) == 0:
        raise ValueError("Нет переданных векторов")

    # Преобразуем входные векторы в массив NumPy
    vectors = [np.array(vector) for vector in vectors]

    # Проверяем, что все векторы имеют одинаковую длину
    if not all(len(vector) == len(vectors[0]) for vector in vectors):
        raise ValueError("Все векторы должны иметь одинаковую длину")

    # Вычисляем расстояния между парами векторов
    distances = []
    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            distance = np.linalg.norm(vectors[i] - vectors[j])
            distances.append(distance)

    # Находим минимальное и максимальное расстояние
    min_distance = min(distances)
    max_distance = max(distances)

    return (min_distance, max_distance)

# Пример использования
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
vector3 = [7, 8, 9]

min_dist, max_dist = min_max_dist(vector1, vector2, vector3)
print("Минимальное расстояние:", min_dist)
print("Максимальное расстояние:", max_dist)








"""
Напишите функцию min_max_dist(*vectors), которая принимает на вход неограниченное число 
векторов через запятую. Гарантируется, что все векторы, которые передаются, одинаковой длины.

Функция возвращает минимальное и максимальное расстояние между векторами в виде кортежа.

Пример


vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])

min_max_dist(vec1, vec2, vec3)
# (5.196152422706632, 10.392304845413264)
"""