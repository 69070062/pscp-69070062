"""Clr"""

col1 = input()
col2 = input()


if col1 in ("Red") and col2 in ("Yellow"):
    print("Orange")
elif col1 in ("Yellow") and col2 in ("Red"):
    print("Orange")
elif col1 in ("Blue") and col2 in ("Yellow"):
    print("Green")
elif col1 in ("Yellow") and col2 in ("Blue"):
    print("Green")
elif col1 in ("Red") and col2 in ("Blue",):
    print("Violet")
elif col1 in ("Blue") and col2 in ("Red",):
    print("Violet")
elif col1 in ("Red") and col2 in ("Red") :
    print("Red")
elif col1 in ("Yellow") and col2 in ("Yellow") :
    print("Yellow")
elif col1 in ("Blue") and col2 in ("Blue") :
    print("Blue")
else :
    print("Error")
