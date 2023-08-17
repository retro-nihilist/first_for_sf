

old_list = ['1', '2', '3', '4', '5', '6', '7']
## new_list = [1, 2, 3, 4, 5, 6, 7]

old_list = ['101', '203', '33', '45', '51', '46', '77']
## new_list = [101, 203, 33, 45, 51, 46, 77]


new_list = list(map(int,old_list))
print(new_list)

