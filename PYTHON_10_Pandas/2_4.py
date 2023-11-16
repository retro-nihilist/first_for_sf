"""В аптеку поступают партии лекарств. Их названия находятся в списке names,
количество единиц товара находится в списке counts.

Например:
names=['chlorhexidine', 'cyntomycin', 'afobazol']
counts=[15, 18, 7]
Напишите функцию create_medications(names, counts), создающую Series medications,
индексами которого являются названия лекарств names, а значениями — их количество в партии counts.

Также напишите функцию get_percent(medications, name), которая возвращает долю товара с именем name
от общего количества товаров в партии в процентах."""

import pandas as pd

def create_medications(names, counts):
    medications = pd.Series(data = counts, index = names)
    return medications #индексами которого являются названия лекарств names, а значениями — их количество в партии counts.


def get_percent(medications, name):
    medications_len = len(medications)
    #print( medications_len)
    counts_sum = sum(medications.iloc[:medications_len])
    part = medications.loc[name] * 100 / counts_sum
    return part #олю товара с именем name от общего количества товаров в партии в процентах


names=['chlorhexidine', 'cyntomycin', 'afobazol']
counts=[15, 18, 7]

medications = create_medications(names, counts)
print(get_percent(medications, "chlorhexidine"))
#print(get_percent(medications, "chlorhexidine")) #37.5

#print(medications)
