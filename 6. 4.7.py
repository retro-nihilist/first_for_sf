def sum_min_numbers(a,b,c):
#def find_min_number(x,y,z):
    x=a; y=b; z=c
    if x>y and x>z: return y+z
    if y>x and y>z: return x+z
    if z>x and z>y: return x+y
print(sum_min_numbers(a = -1, b = 0, c = 10))
#print(find_min_number(10.9, 12.2, 18.4))