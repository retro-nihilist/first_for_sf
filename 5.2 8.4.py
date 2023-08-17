data = [(0.00632, 6.575, 65.2, 296.0, 4.98),
 (0.02731, 6.421, 78.9, 242.0, 9.14),
 (0.02729, 7.185, 61.1, 242.0, 4.03),
 (0.03237, 6.998, 45.8, 222.0, 2.94),
 (0.06905, 7.147, 54.2, 222.0, 5.33),
 (0.02985, 6.43, 58.7, 222.0, 5.21),
 (0.08829, 6.012, 66.6, 311.0, 12.43)]


test=dict()
def persent (x):
    #print("x",x)
    one, two, thry, four, five = x
    six = round(one * four * five, 2)
    return (one, two, thry, four, five, six)
    
lambda_filter = lambda x: x[5] > 60
filtered_data = list(filter(lambda_filter, list(map(persent, data))))

print(filtered_data)

"""
Добавьте в набор данных новый признак, который будет равен
произведению трёх признаков — x₁, x₄ и x₅. 
А затем выберите из исходного списка только те данные, 
для которых значение нового признака > 60.

В результате выполнения программы у вас должен получиться 
список кортежей. Каждый кортеж должен состоять из шести 
элементов: первые пять — исходные признаки, а шестой элемент — сгенерированный признак, округлённый до двух знаков после запятой. Результирующий список кортежей занесите в переменную filtered_data.

Например, для исходного списка data, представленного выше,
 у вас должен получиться следующий список filtered_data:


[(0.02731, 6.421, 78.9, 242.0, 9.14, 60.41),
 (0.06905, 7.147, 54.2, 222.0, 5.33, 81.7),
 (0.08829, 6.012, 66.6, 311.0, 12.43, 341.31)]

Вернёмся к задаче по оценке стоимости недвижимости.

В списке data представлены усреднённые данные по домам в районах Бостона. Каждый вложенный в список кортеж описывает средние данные по одному району (для примера представлены данные о семи участках). В этом кортеже представлены следующие признаки (в порядке следования):

x₁ — уровень преступности на душу населения по городам;
x₂ — среднее количество комнат в доме;
x₃ — доля зданий, построенных до 1940 г. и занимаемых 
владельцами;
x₄ — полная ставка налога на имущество за каждые 10 000 
долларов стоимости;
x₅ — процент населения с низким статусом."""