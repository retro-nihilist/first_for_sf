input_string = input('Введите последовательность чисел: ')
def find_median(input_string):
    import statistics #импортируем
    try:
        temp_list_lmd = lambda input_string: input_string.split(", ")#создаём список из строки
        global return_str#глобализируем строку, которую выведем в случаи успеха
        #создаём Числовой список с введёнными данными и находим медиану и создаём строку для вывода
        return_str = str("Median: " + str(statistics.median((map(int, temp_list_lmd(input_string))))))
        return return_str #возвращаем Медиану
    except ValueError:
        return#возвращаем none в случаи НЕ успеха
print("Некорректный ввод" if find_median(input_string) == None else return_str)


"""Ввод:
1, 5, 2, 3, 6

Вывод:
Median: 3.0
```
```
Ввод:


Вывод:
Median: 4.5
```
```
Ввод:

Вывод:
Некорректный ввод
```
```
Ввод:
десять, 10, пять, 7, семь

Вывод:
Некорректный ввод
```"""