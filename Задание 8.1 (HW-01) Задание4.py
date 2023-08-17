number_word_dict = {
    "ты": 1000, "м": 1000000,
    "сто": 100, "двес": 200, "трис": 300, "четырес": 400, "пятьс": 500, "шестьс": 600, "семьс": 700, "восемьс": 800, "девятьс": 900,
    "одинн": 11, "двен": 12, "трин": 13, "четырн": 14, "пятн": 15, "шестн": 16, "семн": 17, "восемн": 18, "девятн": 19,
    "двад": 20, "трид": 30, "сор": 40, "пятьд": 50, "шестьд": 60, "семьд": 70, "восемьд": 80, "девяно": 90,
    "дес": 10, "н": 0, "о": 1, "дв": 2, "т": 3, "ч": 4, "п": 5, "ш": 6, "с": 7, "в": 8, "д": 9, }

number_word_list = list(number_word_dict.keys())
#print(number_word_list)
my_dict = {}
input_string = "три милиона семьсот восемьдесят три тысячи девятьсот девятнадцать"#input('Введите число словами: ')

dict_itig =dict()
temp_list = list()
def transform_string_to_integer(input_string):
    input_list = input_string.split(sep=" ")#трансформируем строку в список из слов
    #print(input_list)
    for i in input_list:#перебираем слова в ведённом списке
        itr, fix = 0, 0   #счётчики
        while fix<1: # цикл поиска ключей из number_word_dict в введённом списке числительных
            word_list = number_word_list[itr] # выбираем ключь из number_word_dict
            if i.startswith(word_list) == True: # проверка присутствия ключа в введённом списке 
                word_dick = number_word_dict[word_list] # 
                #print("word_list = ", word_list)
                if word_list == "ты" or word_list == "м": # проверка на наличие разрядности
                        dict_itig[word_dick] = list(temp_list)
                        temp_list.clear()
                        #print("dict_itig = ", dict_itig)
                else:
                    temp_list.append(word_dick)
                    #print("temp_list = ", temp_list)
                fix = fix + 1              
            itr = itr + 1
    itog=sum(temp_list)
    for a in dict_itig:
         itog = itog + a * sum(dict_itig[a])
         #print(itog)
    return itog

print(transform_string_to_integer(input_string))

"""number_word_dict_dict = {"mln":{"м": 1000000}, "ths":{"ты":1000},
    "hun":{"сто": 100, "двес": 200, "трис": 300, "четырес": 400, "пятьс": 500, "шестьс": 600, "семьс": 700, "восемьс": 800, "девятьс": 900},
    "dec":{"двад": 20, "трид": 30, "сор": 40, "пятьд": 50, "шестьд": 60, "семьд": 70, "восемьд": 80, "девяно": 90,},
    "tens":{"одинн": 11, "двен": 12, "трин": 13, "четырн": 14, "пятн": 15, "шестн": 16, "семн": 17, "восемн": 18, "девятн": 19},
    "dig": {"дес": 10, "н": 0, "о": 1, "дв": 2, "т": 3, "ч": 4, "п": 5, "ш": 6, "с": 7, "в": 8, "д": 9, }}"""


"""                for d in number_word_dict_dict:
                    if word_list in number_word_dict_dict[d]:
                        #d[word_list]
                        print(number_word_dict_dict[d][word_list])    """


#s.startswith(word)

"""
**Пример №1:**
Ввод:
один
Вывод:
1

**Пример №2:**
Ввод:
двадцать
Вывод:
20

**Пример №3:**
Ввод:
двести сорок шесть
Вывод:
246

**Пример №4:**
Ввод:
 семьсот восемьдесят три тысячи девятьсот девятнадцать
Вывод:
783919
"""
"""
if word_list == "м":
    key_dict["м"]

    key_list1.append(key_list0)
elif word_list == "ты":
    key_list1.append(key_list0)
elif word_list == "сто"or"двес"or"трис"or"четырес"or"пятьс"or"шестьс"or"семьс"or"восемьс"or"девятьс":




if "ты"

if "сто": 100, "двес": 200, "трис": 300, "четырес": 400, "пятьс": 500, "шестьс": 600, "семьс": 700, "восемьс": 800, "девятьс": 900,
if "двад": 20, "трид": 30, "сор": 40, "пятьд": 50, "шестьд": 60, "семьд": 70, "восемьд": 80, "девяно": 90,
if "одинн": 11, "двен": 12, "трин": 13, "четырн": 14, "пятн": 15, "шестн": 16, "семн": 17, "восемн": 18, "девятн": 19,
"""