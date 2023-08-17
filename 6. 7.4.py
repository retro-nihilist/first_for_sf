cheese_data = {
    'чеддер': [370, 5000, 33, 'твердый'],
    'пармезан': [510, 4000, 29, 'твердый'],
    'гауда': [250, 3700, 27, 'полутвердый'],
    'эдам': [220, 10000, 30, 'полутвердый'],
    'горгонзола': [320, 3000, 32, 'полумягкий'],
    'рокфор': [340, 15000, 31, 'полумягкий'],
    'стилтон': [360, 7000, 35, 'полумягкий'],
    'камамбер': [250, 8000, 24, 'мягкий'],
    'бри': [310, 6500, 28, 'мягкий'],
}
cheese_data_list = []
def sort_cheese(cheese_data):
    #cheese_data_list = list(cheese_data.items())
    #print(cheese_data_list)
    for k, v in cheese_data.items():
        temp_list = []
        temp_list.append(k)
        temp_list.append(v[0])
        cheese_data_list.append(temp_list)
        #print(temp_list)
    cheese_data_list2 = []
    #print(cheese_data_list)
    cheese_data_list.sort(key=lambda i: i[1])
    for k in cheese_data_list: cheese_data_list2.append(k[0])
    #print(cheese_data_list2)
    #print(cheese_data_list)
    return cheese_data_list2
    #print(cheese_data_list)
    #return sorted(cheese_data_list, key=lambda student: student[1])
    #return cheese_data_list

print(sort_cheese(cheese_data))
# ['эдам', 'гауда', 'камамбер', 'бри', 'горгонзола', 'рокфор', 'стилтон', 
# 'чеддер', 'пармезан']