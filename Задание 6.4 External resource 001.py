    #-------------------------------------------------------
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
    #-------------------------------------------------------