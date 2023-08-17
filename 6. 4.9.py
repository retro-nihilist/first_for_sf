def get_prediction(x1,x2):
    if x1<20:
        if x2<200:
            return 300.5
        else: return 65.7
    else:
        if x2<170:
            if x1<40:
                return -64.1
            else: return 0.7
        else: return 1023





print(get_prediction(x1=15, x2=150))
# 300.5
print(get_prediction(x1=15, x2=350))
# 65.7
print(get_prediction(x1=35, x2=100))
# -64.1
print(get_prediction(x1=175, x2=100))
# 0.7
print(get_prediction(x1=175, x2=200))
# 1023