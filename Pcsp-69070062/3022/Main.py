"""Temp"""
temp =input().upper()
ten = input().upper()
ten2 = input().upper()

if ten in "C" and ten2 in "F" :
    print(f"{(float(temp) * 9 / 5 + 32):.2f}")

elif ten in "F" and ten2 in "C" :
    print(f"{(float(temp) - 32) * 5 / 9:.2f}")

elif ten in "C" and ten2 in "K" :
    print(f"{(float(temp) + 273.15):.2f}")

elif ten in "K" and ten2 in "C" :
    print(f"{(float(temp) - 273.15):.2f}")

elif ten in "F" and ten2 in "K" :
    print(f"{(float(temp) - 32) * 5 / 9 + 273.15:.2f}")

elif ten in "K" and ten2 in "F" :
    print(f"{(float(temp) - 273.15) * 9 / 5 + 32:.2f}")

elif ten in "C" and ten2 in "R" :
    print(f"{(float(temp) + 273.15) * 9 / 5:.2f}")

elif ten in "R" and ten2 in "C" :
    print(f"{(float(temp) - 491.67) * 5 / 9:.2f}")

elif ten in "F" and ten2 in "R" :
    print(f"{(float(temp) + 459.67):.2f}")

elif ten in "R" and ten2 in "F" :
    print(f"{(float(temp) - 459.67):.2f}")

elif ten in "K" and ten2 in "R" :
    print(f"{(float(temp) * 9 / 5):.2f}")

elif ten in "R" and ten2 in "K" :
    print(f"{(float(temp) * 5 / 9):.2f}")

elif ten in "C" and ten2 in "C" :
    print(f"{(float(temp)):.2f}")

elif ten in "F" and ten2 in "F" :
    print(f"{(float(temp)):.2f}")

elif ten in "K" and ten2 in "K" :
    print(f"{(float(temp)):.2f}")

elif ten in "R" and ten2 in "R" :
    print(f"{(float(temp)):.2f}")
