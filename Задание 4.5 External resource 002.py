# Функция для регистрации пользователей

# Функция для проверки корректности даты
def check_date(day, month, year):
    def is_leap(year):
        if year%400==0:
            r=True
        elif year%100==0:
            r=False
        elif year%4==0:
            r=True
        else:
            r=False
        #print ("r400 = ", r)
        return r
    # Проверяем день, месяц и год на целочисленность
    if (type(day) is not int) or (type(month) is not int) or (type(year) is not int):
        return False
    # Проверяем год на заданный диапазон
    if (year <= 1900) or (year >= 2022):
        return False
    # Проверяем месяц на заданный диапазон     
    if (month < 1) or (month > 12):
        return False
    # Проверяем день на заданный диапазон  
    if (day < 1) or (day > 31):
        return False
    # Проверяем апрель, июнь, сентябрь и ноябрь на количество дней
    if (month in [4,6,9,11]) and (day > 30):
        return False
    # Проверяем количество дней в феврале
    if (month == 2) and (day > 28) and (is_leap(year)==False):
        return False
    if (month == 2) and (day > 29) and (is_leap(year)==True):
        return False            
    return True

def register(surname, name, date, middle_name=None, registry=None):
    # Вспомогательная функция для предобработки даты
    def preprocessing_date(date):
        # Разделяем строку по символу точки
        day, month, year = date.split('.')
        # Преобразуем все данные к типу данных int
        day, month, year = int(day), int(month), int(year)
        return day, month, year
    # Если список не был передан — создаём пустой список
    if registry is None:
        registry = list()
    # Разделяем дату на составляющие
    day, month, year = preprocessing_date(date)
    #------------------------------------------------------------------------------------

    #------------------------------------------------------------------------------------
    if check_date(day, month, year) == False:
        raise ValueError("Invalid Date!")
    else:
    # Добавляем данные в список
        registry.append((surname, name, middle_name, day, month, year))
        return registry
## Вызываем функцию для регистрации
# Если список registry не передаётся, то он создаётся внутри функции
reg = register('Petrova', 'Maria', '13.03.2003', 'Ivanovna')
reg = register('Ivanov', 'Sergej', '24.09.1995', registry=reg)
reg = register('Smith', 'John', '13.113.2003', registry=reg)
print(reg)
