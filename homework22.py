prize = float(input('Чё по чём? '))
size = 0.35
if prize > 20:
    sale = prize*size
    summ = prize-sale
    print('Тебе повезло, так и быть. Скидка ', round(sale, 2), ' Плати ', round(summ, 2))
else:
    print('Слишком мало, нищий. Плати ', prize)