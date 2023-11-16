"""Напишите функцию task_manager(tasks), которая принимает список задач tasks для нескольких серверов.
Каждый элемент списка состоит из кортежа (<номер задачи>, <название сервера>, <высокий приоритет задачи>).
Функция должна создавать словарь и заполнять его задачами по следующему принципу: название сервера — ключ,
по которому хранится очередь задач для конкретного сервера.
Если поступает задача без высокого приоритета (последний элемент кортежа — False), добавить номер задачи
 в конец очереди. Если приоритет высокий, добавить номер в начало.
Для словаря используйте defaultdict, для очереди — deque.
Функция возвращает полученный словарь с задачами.
print(task_manager(tasks))
# defaultdict(, {'voltage': deque([41667, 35364]), 'office': deque([36871, 40690, 33850])} )
"""
from collections import deque
from collections import defaultdict

tasks = [(36871, 'office', False),
         (40690, 'office', False),
         (35364, 'voltage', False),
         (41667, 'voltage', True),
         (33850, 'office', False)]

def task_manager(tasks):

    servers = list(set(item[1] for item in tasks))

    for name in servers:
        exec(f'{name} = []')

    itog_dict = defaultdict(deque)  # Используем defaultdict с типом deque

    for i in tasks:
        if i[2] == True:
            itog_dict[i[1]].appendleft(i[0])
        else:
            itog_dict[i[1]].append(i[0])

    return itog_dict

result = task_manager(tasks)
print(result)