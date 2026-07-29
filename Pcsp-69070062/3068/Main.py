"""29"""

def main():
    """29"""
    x = int(input())

    if not x % 400 :
        print("yes")
    elif not x % 100 and x > 1582:
        print("no")
    elif not x % 100 and x <= 1500:
        print("yes")
    elif not x % 4 :
        print("yes")
    else :
        print("no")
main()
