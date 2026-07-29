"""swp"""

def main():
    """swp"""
    num = int(input())
    op = input()

    swap = int(str(num)[::-1])

    if op == "+":
        print(num, "+", swap, "=", num + swap)
    else:
        print(num, "*", swap, "=", num * swap)
main()
