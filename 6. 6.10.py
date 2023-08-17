lst=[]
def find_video(data):
    lst_lambda = lambda x: lst.append(x)
    for i in data:
        if i == "videoID":
            lst_lambda(data.get(i))
            #print(data.get(i))
        if type(data.get(i)) == dict:
            #print("find_dict", data.get(i))
            find_video(data.get(i))
        if type(data.get(i)) == list:
            #print("find_list", data.get(i))
            for i in data.get(i):
                if type(i)==dict:
                    find_video(i)
    return lst
            
data = {
    "type": "video",
    "videoID": "vid001",
    "links": [
        {"type":"video", "videoID":"vid002", "links":[]},
        {   "type":"video",
            "videoID":"vid003",
            "links": [
            {"type": "video", "videoID":"vid004"},
            {"type": "video", "videoID":"vid005"},
            ]
        },
        {"type":"video", "videoID":"vid006"},
        {   "type":"video",
            "videoID":"vid007",
            "links": [
            {"type":"video", "videoID":"vid008", "links": [
                {   "type":"video",
                    "videoID":"vid009",
                    "links": [{"type":"video", "videoID":"vid010"}]
                }
            ]}
        ]},
    ]
}
print(find_video(data))
"""Дан словарь data, содержащий в себе несколько вложенных структур данных. Некоторые из 
них (независимо от вложенности) содержат ключ "videoID". Значениями для таких ключей 
являются идентификаторы видео.

Напишите рекурсивную функцию, которая извлекает все значения с ключом "
videoID". Функция должна принимать на вход словарь data и возвращать список из 
найденных идентификаторов видео.

Например, при вызове функции find_video() для следующего словаря:
мы должны получить результат:


['vid001', 'vid002', 'vid003', 'vid004', 'vid005', 'vid006', 'vid007', 'vid008', 'vid009', 'vid010']"""