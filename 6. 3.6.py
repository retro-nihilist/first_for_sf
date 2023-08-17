lst = [0, 0, 1, 2, 3, 4, 5, 5, 6, 7]

# True

lst = list(range(0, 15))

# False

def check_duplicates(z):
    set_duplicates = set(lst)
    duplicates = lambda x, y: True if len(x) > len(y) else False
    return duplicates (lst, set_duplicates)

print(check_duplicates(lst))