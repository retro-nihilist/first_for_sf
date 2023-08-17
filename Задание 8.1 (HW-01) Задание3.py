import statistics
input_string = input('Введите последовательность чисел: ')
def find_median(input_string):
    #input_list0 = list()
    try:
        temp_list_lmd = lambda input_string: input_string.split(", ")#создаём список из строки
        return "Median:" + str(statistics.median((map(int, temp_list_lmd(input_string)))))#создаём Числовой список с введёнными данными)
    except ValueError:
        print("Некорректный ввод")
        return

print(find_median(input_string))


"""Ввод:
1, 5, 2, 3, 6

Вывод:
Median: 3.0
```
```
Ввод:
100, 5, 2, 4, 3, 6

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