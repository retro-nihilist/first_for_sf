import string
alphabet = list(string.ascii_lowercase + "a") #Добавляем "a" для отработки символа "z"  

s = "zzzzqscbbbb" #input('Введите строку: ')
s_list=list(s)#переводим строку в список
def unikum(s_list):
    s_set = set(s_list)#создаем набор уникальных символов в исходной строке
    if len(set(s_list)) < len(s_list):#проверяем список на наличие дубликатов
        for i in s_set:#Если дубликаты есть то проверяем стоку
            if s_list.count(i) > 1:#если в строке есть повторения символов
                s_list.remove(i)#удаляем первый дубликат
                s_list[s_list.index(i)] = alphabet[alphabet.index(i)+1]#Заменяем второй дубликат на следующий алфавитный символ
                unikum(s_list)#используем рекурсию для работы функции с новым списком
        else:
            return ''.join(s_list) # преобразовываем список в строку и возврвщаем результат

print(unikum(s_list))    
        
        
        