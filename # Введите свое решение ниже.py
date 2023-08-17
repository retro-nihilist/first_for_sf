# Введите свое решение ниже
#hyp = lambda a, b:(a**2 + b**2) ** (1/2)

#l_in=[]
itog=[]
def sort_sides (l_in):
    a=0
    for i in l_in:
        #print(i[0])
        #print(i[1])
        #print(a)
        x = (i[0]**2 + i[1])**(1/2)
        #print(x)
        #print(itog)
        itog.append(x)
        a+=1
    itog.sort()
    return itog


hyp = lambda a, b:(a**2 + b**2) ** (1/2)

print(sort_sides([(3,4), (1,2), (10,10)]))