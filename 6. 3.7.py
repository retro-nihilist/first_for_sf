#print(swap_places([1, 2, 3]))
## [3, 2, 1]
#print(swap_places([1, 2, 3, 4, 5]))
## [5, 2, 3, 4, 1]
#rint(swap_places(['н', 'л', 'о', 'с']))
## ['с', 'л', 'о', 'н']

def swap_places(x):
    x0=x[0]
    i_end = len(x)-1
    x_end=x[i_end]
    x[0]=x_end
    x[i_end]=x0
    return x

print(swap_places(['н', 'л', 'о', 'с']))
## ['с', 'л', 'о', 'н']