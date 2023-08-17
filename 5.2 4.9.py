d={'radius':0, 'circumference':0, 'area':0}
def circle(p1,p2):
    # Распаковываем кортежи для удобства, “;” означает новую строку кода
    x1, y1 = p1; x2, y2 = p2
    # Вычисляем стороны по теореме Пифагора
    r = ((x2 - x1) ** 2 + (y2 - y1)** 2) ** 0.5
    d['radius']=round(r,3)

    def calculate_circumference(r):
        #функция для вычисления длины окружности
        d['circumference']=round(2*pi*r,3)

    def calculate_area_circle(r):
        #ункция для вычисления площади окружности
        d['area']=round(pi*r**2, 3)

    calculate_circumference(r)
    calculate_area_circle(r)
    return d

pi = 3.1416
print(circle(p1=(3, 2.5), p2=(4, 4.5)))
## {'radius': 2.236, 'circumference': 14.05, 'area': 15.708}

pi = 3.1416
print(circle(p1=(0, 0), p2=(1, 1)))
## {'radius': 1.414, 'circumference': 8.886, 'area': 6.283}

pi = 3.14
print(circle(p1=(3, 2.5), p2=(4, 4.5)))
## {'radius': 2.236, 'circumference': 14.043, 'area': 15.7}