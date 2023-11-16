"""Дан список кортежей ratings с рейтингами кафе. Кортеж состоит из названия и рейтинга кафе.
Необходимо отсортировать кортеж по убыванию рейтинга. Если рейтинги совпадают, то отсортировать
 кафе дополнительно по названию в алфавитном порядке.
Получите словарь cafes с упорядоченными ключами из отсортированного списка, где ключи — названия кафе,
 а значения — их рейтинг.
"""
from collections import OrderedDict
ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]

dict_ratings = OrderedDict(dict(ratings))

cafes = OrderedDict(sorted(dict_ratings.items(), key=lambda item: (-item[1], item[0])))
print(cafes)



