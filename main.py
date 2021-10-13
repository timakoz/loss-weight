#################
#
# TODO: 
#
#################
import math
import random



p = 0
lessed = 0
needlesskkal = 5 * 7000
c = 10
while c > 0:
    if p == 3:
        z = 2000
    else:
        z = 2200
    day = random.randint(1000,z)
    if day > 2000:
        p += 1
    c -= 1
    lessed += 2000 - day

lessed /= 7000

print ('Так держать вы сбросили (кг): ', round(lessed,2), 'Осталось еще: ', round(5 - lessed, 2))












#ordinarykkal = 2000 * days