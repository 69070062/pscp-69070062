"""sur"""


max = float(input())
high = float(input())


avg = (max - high) / 2
if high >= avg + 2:
    print("Surprising")
else:
    print("Not surprising")
