
def get_words_list(text):
    punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
    for i in punctuation_list: text = text.replace(i, "")
    text = list(text.lower().split(" "))
    return text

text_example = "Arrakis, the planet known as Dune, is forever his place."

print(get_words_list(text=text_example))

""
"""
Напишите функцию get_words_list(), которая:

избавляется от знаков препинания в тексте,
приводит текст к нижнему регистру,
возвращает список из слов в тексте.
Текст, к которому необходимо применить предобработку, передаётся в функцию в виде аргумента text.

Для решения задачи вы можете использовать готовый список со знаками препинания:


punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
Сделайте этот список локальной переменной функции get_words_list().

Пример работы программы:


text_example = "Arrakis, the planet known as Dune, is forever his place."

print(get_words_list(text=text_example))
# ['arrakis', 'the', 'planet', 'known', 'as', 'dune', 'is', 'forever', 'his', 'place']
"""