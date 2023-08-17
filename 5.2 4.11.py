d={'a': 0, 'b': 0, 'length': 0, 'area': 0}
def ellipse(p1, p2, p3):

    # Распаковываем кортежи для удобства, “;” означает новую строку кода
    x1, y1 = p1; x2, y2 = p2; x3, y3 = p3
    # Вычисляем стороны по теореме Пифагора
    a = round(((x2 - x1) ** 2 + (y2 - y1)** 2) ** 0.5, 3)
    b = round(((x3 - x1) ** 2 + (y3 - y1)** 2) ** 0.5, 3)
    d['a']=a
    d['b']=b

    def calculate_area_ellipse(a,b):
        #функция для вычисления площади эллипса
        d['area']=round(pi*a*b, 3)
        return

    def calculate_length_ellipse(a,b):
        #функция для вычисления длины окружности эллипса
        d['length']=round(2*pi*((a**2 + b**2)/2)**0.5, 3)
        return
    
    calculate_area_ellipse(a,b)
    calculate_length_ellipse(a,b)
    return d
    


pi = 3.1416
print(ellipse(p1=(3, 2.5), p2=(4.5, 2.5), p3=(3, 3.5)))

## {'a': 1.5, 'b': 1.0, 'length': 8.01, 'area': 4.712}

pi = 3.1416
print(ellipse(p1=(0, 0), p2=(0, 1), p3=(1, 0)))

## {'a': 1.0, 'b': 1.0, 'length': 6.283, 'area': 3.142}

pi = 3.14
print(ellipse(p1=(0, 0), p2=(0, 1), p3=(1, 0)))
## {'a': 1.0, 'b': 1.0, 'length': 6.28, 'area': 3.14}