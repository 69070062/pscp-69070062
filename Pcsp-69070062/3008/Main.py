"""Alexandria"""

a = float(input())
b = float(input())
c = float(input())

s = (a + b + c) / 2

area = f"{(s * (s - a) * (s - b) * (s - c)) ** 0.5 :.3f}"

print(area)
