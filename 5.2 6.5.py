def power(val, n):

    x=val
    if n==0: return 1
    if n==1: return val
    for i in range(n-1):
        x=val*x
    return x




print(power(25, 0))
# 1
print(power(-5, 4))
# 625