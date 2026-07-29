"""Wan"""

r,x,y = map(int,input().split())
posi = x**2 + y**2
radi = r**2
if posi < radi :
    print("IN")
elif posi == radi :
    print("ON")
else :
    print("OUT")
