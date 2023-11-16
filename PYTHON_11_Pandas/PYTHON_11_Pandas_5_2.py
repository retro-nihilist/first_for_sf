import os
import pandas as pd
print_id =1
os.chdir(r'C:\unique_data\rep_fo_sf\PYTHON_11_Pandas\data')
melb_data_ps = pd.read_csv('melb_data_ps.csv', sep= ",")
#melb_data_ps.info()
melb_df = melb_data_ps.copy()

"""Задание 5.2
1 point possible (graded)
При преобразовании столбцов таблицы о недвижимости к типу category мы оставили без внимания столбец Suburb (пригород). Давайте исправим это.
С помощью метода info() узнайте, сколько памяти занимает таблица melb_df.
Преобразуйте признак Suburb следующим образом: оставьте в столбце только 119 наиболее популярных пригородов, остальные замените на 'other'.
Приведите данные в столбце Suburb к категориальному типу.
В качестве ответа запишите разницу между объёмом занимаемой памяти до преобразования (который мы получили ранее в модуле) и после него в Мб.
Ответ округлите до десятых."""

"""С помощью метода info() узнайте, сколько памяти занимает таблица melb_df."""
melb_df.info()
memory_usage_0 = melb_df.memory_usage(deep=True).sum()
print(memory_usage_0 / (1024*1024))

"""Преобразуйте признак Suburb следующим образом: оставьте в столбце только 119 наиболее популярных пригородов,
остальные замените на 'other'."""
Suburb = melb_df['Suburb']#получаем серию
#display(SellerG.value_counts())
popular_Suburb = Suburb.value_counts().nlargest(119).index#из серии получаем количества уникальных значений и делаем срез
#print(popular_Suburb)

"""а остальные обозначьте как 'other'."""
melb_df['Suburb'] = Suburb.apply(lambda x: x if x in popular_Suburb else 'other')
#melb_df.info()

"""Приведите данные в столбце Suburb к категориальному типу."""
melb_df['Suburb'] = melb_df['Suburb'].astype('category') # преобразуем тип столбца
#display(melb_df['Suburb'].cat.codes)
#print(melb_df['Suburb'].cat.categories)
#melb_df.info()
memory_usage_1 = melb_df.memory_usage(deep=True).sum()
print(memory_usage_1 / (1024*1024))
print((memory_usage_0 - memory_usage_1) / (1024*1024))