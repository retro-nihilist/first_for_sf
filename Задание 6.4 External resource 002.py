new_list = ['111', '00','222', '55555',  'c22']
#new_list.sort(key=lambda word: len(word))
#print(new_list)
# Будет напечатано:
# ['cc', 'bbb', 'aaa', 'ababa', 'aaaaa']

#Как видите, слова отсортированы по длине

new_list.sort(key=lambda word: (len(word), word))
print(new_list)
# Будет напечатано:
# ['cc', 'aaa', 'bbb', 'aaaaa', 'ababa']