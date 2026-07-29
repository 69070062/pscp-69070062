"""Milk"""

def main():
    """Milk"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    milk = d // a

    if b:
        if milk >= b:
            exchange = (milk - b) // (b - c) + 1
            milk += exchange * c

    print(milk)

main()
