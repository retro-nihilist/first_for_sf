import os
import pandas as pd
print_id =1

"""import os.path
print(os.path.isfile("data/melb_data.csv"))
print(os.path.isfile('data/melb_data.csv'))
print(os.path.exists('PYTHON_10_Pandas'))

current_directory = os.getcwd()# Получаем текущую директорию
if print_id > 0: print("current_directory = ", current_directory)
print(os.path.abspath("5.py"))
print(os.path.basename("5.py"))
print("os.path.dirname = ",os.path.dirname("5.py"))
print(os.path.dirname('PYTHON_10_Pandas'))"""

os.chdir(r'C:\unique_data\rep_fo_sf\PYTHON_10_Pandas\data')
melb_data = pd.read_csv('melb_data.csv', sep= ",")

ser = melb_data.Price
print(ser.iloc[15])

ser = melb_data.Date
print(ser.iloc[90])

ser1 = melb_data.Landsize
print(ser1.iloc[3521])
ser2 = melb_data.BuildingArea
print(ser2.iloc[1690])
print(ser1.iloc[3521] / ser2.iloc[1690])
display(melb_data.head())


"""https://ru.stackoverflow.com/questions/898532/%D0%9A%D0%B0%D0%BA-%D0%B2-python-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D0%BF%D1%83%D1%82%D1%8C-%D0%BA-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D0%BD%D1%8F%D0%B5%D0%BC%D0%BE%D0%BC%D1%83-%D1%84%D0%B0%D0%B9%D0%BB%D1%83"""
"""from os.path import abspath
abspath(__file__)

current_directory = os.getcwd()# Получаем текущую директорию
if print_id > 0: print("current_directory = ", current_directory)

relative_path = "data\melb_data.csv"# Определяем относительный путь к файлу melb_data.csv
if print_id > 0: print("relative_path = ", relative_path)

file_path = os.path.join(current_directory, relative_path)# Составляем абсолютный путь к файлу на основе текущей директории и относительного пути
if print_id > 0: print("file_path = ", file_path)

#melb_data = pd.read_csv(file_path)# Чтение данных из CSV файла и помещение их в переменную melb_data
"""

"""from pathlib import Path
relative_path = "data/melb_data.csv"# Определяем относительный путь к файлу melb_data.csv
if print_id > 0: print("relative_path = ", relative_path)
file_path = Path(relative_path)# Создаем объект Path с относительным путем
if print_id > 0: print("file_path = ", file_path)
#melb_data = pd.read_csv(file_path)# Чтение данных из CSV файла и помещение их в переменную melb_data
#if print_id > 0: print("melb_data = ", melb_data)"""
