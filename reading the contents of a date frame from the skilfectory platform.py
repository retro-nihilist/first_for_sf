#reading the contents of a date frame from the skilfectory platform
"""Код для чтения содержимого дата фрейма из платформы скилфектори"""

import pandas as pd
import numpy as np
from io import StringIO
# Введите свое решение ниже
with open('test_sber_data.csv', 'r') as file:
    file_contents = file.read()
#print(file_contents)
# Чтение текста в DataFrame
df = pd.read_csv(StringIO(file_contents), skipinitialspace=True)
# Вывод DataFrame
print(df)