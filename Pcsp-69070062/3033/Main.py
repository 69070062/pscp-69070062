"""Gift"""

radius,high,glue = map(float,input().split())
width = high + (2 * radius)
lengt = (2 * 3.14 * radius) + glue
print(f"{width:.2f} {lengt:.2f}")
