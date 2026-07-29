"""Count"""

x = input()
a =x.count("a") + x.count("A")
e =x.count("e") + x.count("E")
i =x.count("i") + x.count("I")
o =x.count("o") + x.count("O")
u =x.count("u") + x.count("U")

if a > 0:
    print("a" + " : " + str(a))
if e > 0:
    print("e" + " : " + str(e))
if i > 0:
    print("i" + " : " + str(i))
if o > 0:
    print("o" + " : " + str(o))
if u > 0:
    print("u" + " : " + str(u))
