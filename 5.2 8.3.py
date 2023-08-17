reg = [('Ivanov', 'Sergej', 24, 9, 1995),
      ('Smith', 'John', 13, 2, 2003),
      ('Petrova', 'Maria', 13, 3, 2003)]

new_reg = list()
lambda_reg = lambda x: x[4] > 2000
y = list(filter(lambda_reg, reg))

i=0
def lambda_reg_2(i):
    i = list(i)
    i[0] = str(i[0])+" "+ str(i[1][:1])+"."
    i.pop(1)
    i = tuple(i)
    #print(i)
    return i

new_reg = list(map(lambda_reg_2, y))

print("new_reg = ",new_reg)
#new_reg = [('Smith J.', 13, 2 , 2003), ('Petrova M.', 13, 3, 2003)]