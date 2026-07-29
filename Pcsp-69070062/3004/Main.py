"""pleas put in the coordinate for x y z"""


import math

x1 , y1 , z1 =  map(float, input().split())
x2 , y2 , z2 =  map(float, input().split())

re = ((x1 - x2)**2) + ((y1 - y2)**2) + ((z1 - z2)**2)
print(f"{math.sqrt(re):.2f}")
