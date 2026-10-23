""" Prime """


def main():
    """Prime"""
    n = int(input())
    if n < 2:
        print("NO")
        return
    i = 2
    prime = True
    while i * i <= n:
        if not n % i :
            prime = False
            break
        i += 1
    print("YES" if prime else "NO")


if __name__ == "__main__":
    main()
