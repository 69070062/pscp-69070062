"""code"""

char = input()
num = input()

if char in "H" and num in "4567" :
    print("safe unlocked")
elif char in "H":
    print("safe locked - change digit")
elif num in "4567":
    print("safe locked - change char")
else :
    print("safe locked")
