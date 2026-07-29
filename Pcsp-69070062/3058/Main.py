"""Bridge"""

def main():
    """Bridge"""
    a = int(input())
    b = int(input())
    g = int(input())

    big = min(b, g // 5)
    small = g - big * 5

    if small <= a:
        print(small)
    else:
        print(-1)

main()
