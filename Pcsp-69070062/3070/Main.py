"""Odev"""

def main():
    """Odev"""
    x = int(input())
    y = int(input())
    z = int(input())

    even = 0
    odd = 0

    for num in (x, y, z):
        if not num % 2 :
            even += 1
        else:
            odd += 1

    print(even)
    print(odd)

main()
