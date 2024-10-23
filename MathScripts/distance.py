# Question 4. How do you calculate the distance between coordinates (x1,y1) and (x2,y2)?

import math

x1 = 2
y1 = 3
x2 = 6
y2 = 8

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print('The distance between coordinates (' + str(x1) + ',' + str(y1) + ') and (' + str(x2) + ',' + str(y2) + ') is ' + format(distance, ".2f"))