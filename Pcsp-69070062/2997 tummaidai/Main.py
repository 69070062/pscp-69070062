"""elo"""

eloA = input()
eloB = input()
Winner = input()

if Winner in "A" :
    Ea = 1 / (1 + 10 ** ((float(eloB) - float(eloA)) / 400))
    print(f"{Ea:.2f}")
elif Winner in "B " :
    Eb = 1 / (1 + 10 ** ((float(eloA) - float(eloB)) / 400))
    print(f"{Eb:.2f}")
