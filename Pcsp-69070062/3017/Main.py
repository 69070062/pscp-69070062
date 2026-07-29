"""Bills"""

price = int(input())

serv = price * 0.10


if serv >= 1000 :
    serv = 1000
elif serv <= 50 :
    serv = 50

pri2 = price + serv
tax = pri2 * 0.07

print(f"{price + serv + tax:.2f}")
