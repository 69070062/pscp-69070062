"""choose lowest"""

amount = int(input())
numlist = []

while amount > 0:
    x = int(input())
    numlist.append(x)
    amount -= 1

re = sorted(numlist)
print(re[0])
