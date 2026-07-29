"""coin"""

money = int(input())

te = money // 10
ten = money % 10
fiv = ten // 5
five = ten % 5
tw = five // 2
two = five % 2

print("10" + " = " + str(te))
print("5" + " = " + str(fiv))
print("2" + " = " + str(tw))
print("1" + " = " + str(two))
