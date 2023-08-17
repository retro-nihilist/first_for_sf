def lucky_ticket(x):
    ticket_str = str(x)
    d1=list(ticket_str[:3])
    d1=[int(x) for x in d1]
    d2=list(ticket_str[3:])
    d2=[int(x) for x in d2]

    #print (sum(d1), sum(d2))
    return sum(d1)==sum(d2)


#int_lst = [int(x) for x in str_lst]

print(lucky_ticket(111111))
# True
print(lucky_ticket(123456))
# False
"""Напишите функцию lucky_ticket(), которая проверяет, 
является ли билет счастливым.

Примечание. Билет счастливый, если сумма первых
 трёх цифр в его номере равна сумме последних трёх цифр.

На вход функция принимает шестизначное число
 ticket_number и должна возвращать одно из булевых
   значений (True или False) в зависимости от того,
     является ли билет счастливым.

При решении постарайтесь не использовать встроенную 
функцию sum() — примените циклы.

Примеры работы программы:


print(lucky_ticket(111111))
# True
print(lucky_ticket(123456))
# False"""