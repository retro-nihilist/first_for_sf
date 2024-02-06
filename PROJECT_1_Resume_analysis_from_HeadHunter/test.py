import seaborn as sns
import matplotlib.pyplot as plt

# Ваши данные (замените их своими данными)
data_orig = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Создание фигуры и осей
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 4))

# Сначала создаем ящик с усами, не отображая выбросы
boxplot = sns.boxplot(data_orig, ax=axes[1], showfliers=False)

# Затем получаем параметры ящика с усами
lower_whisker = boxplot.lines[0].get_xdata()[0]
upper_whisker = boxplot.lines[1].get_xdata()[0]
lower_box = boxplot.lines[2].get_xdata()
upper_box = boxplot.lines[3].get_xdata()
median = boxplot.lines[4].get_xdata()[0]

# Выводим параметры
print("Нижний ус:", lower_whisker)
print("Верхний ус:", upper_whisker)
print("Нижняя граница коробки:", lower_box[0])
print("Верхняя граница коробки:", upper_box[0])
print("Медиана:", median)

# Второй график (histplot) можете оставить, если нужно

# Показываем график
plt.show()


"""    # Параметры ящика с усами
    box_params = boxplot.get_lines()
    lower_whisker = box_params[0].get_xdata()[0]
    upper_whisker = box_params[1].get_xdata()[0]
    lower_box = box_params[2].get_xdata()
    upper_box = box_params[3].get_xdata()
    median = box_params[4].get_xdata()[0]"""