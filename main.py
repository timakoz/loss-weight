import random
x = 1000
y = 0 # Дни когда Евдокия Артёмовна ест меньше 2000 ккал
lessedall = 0
p = 0 # Дни когда Евдокия Артёмовна ест больше 2000 ккал
lessed = 0
needlesskkal = 5 * 7000
c = 1
while True:
    if p == 2: # Если количество вкусняшек в 10 днях превышает 2 мы убираем шанс их выпадения
        z = 1999
    else:
        z = 2200

    if y == 9:  # Если нет вкусняшек в 9 днях мы принудительно их выдаем
        x = 2000
        z = 2200
    else:
        x = 1000
    
    daykkal = random.randint(x,z)

    print ('День', c, 'Сегодня нужно сьесть: ', daykkal)
    if daykkal >= 2000:
        p += 1
    else:
        y += 1
    c += 1 # текущий день
    lessed += 2000 - daykkal # сколько сбросили ккал сегодня
    
    lessed /= 7000 # переводим в кг
    lessedall = lessedall + lessed
    if c % 10 == 1:
        print ('Так держать! Вы уже сбросили:', round(lessedall,2), 'кг', 'Осталось еще:', round(5 - lessedall, 2), 'кг')
        y = 0
        p = 0
    if lessedall >= 5:
        print ('Поздравляю! Вы сбросили',round(lessedall, 2), 'кг' )
        break
