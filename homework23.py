num = int(input())
month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Недрочабрь', 'Декабрь']
if 1 <= num <= 12:
    print(month[num-1])
else:
    print('Иди учи месяца')