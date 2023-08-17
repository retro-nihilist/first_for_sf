"""Мы анализируем данные об автомобилях. Данные являются табличными и представлены в виде словаря car_data, ключами которого являются параметры:

‘car_ID’ — идентификатор автомобиля;
‘fueltype’ — тип двигателя (бензиновый — 'gas' или дизельный — 'diesel');
‘horsepower’ — мощность двигателя (в лошадиных силах);
‘price’ — стоимость автомобиля.
Значениями словаря являются списки, в которых хранятся значения указанных параметров для каждого из автомобилей. Например, следующий словарь car_dict:
"""

car_dict = {
    'car_ID': [123, 117, 111, 82, 101, 96, 156, 2, 58, 49],
    'fueltype': ['gas', 'diesel', 'diesel', 'gas', 'gas', 'gas', 'gas', 'gas', 'gas', 'gas'],
    'horsepower': [68, 95, 95, 88, 97, 69, 62, 111, 101, 176],
    'price': [7609.0, 17950.0, 13860.0, 8499.0, 9549.0, 7799.0, 8778.0, 16500.0, 13645.0, 35550.0]
}

from statistics import mean
mean_price = mean(car_dict['price'])
count_diesel = car_dict['fueltype'].count('diesel')
min_horsepower = min(car_dict['horsepower'])







"""
mean_price = 13973.9
count_diesel = 2
min_horsepower = 62 
"""