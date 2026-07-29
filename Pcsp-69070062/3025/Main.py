"""w2e"""

Month = int(input())
Day = int(input())

if Day >= 21 and Day <= 31 and Month in (12,) :
    print("winter")
elif Month in (1, 2) :
    print("winter")
elif Day >= 1 and Day <= 20 and Month in (3,) :
    print("winter")
elif Day >= 21 and Day <= 31 and Month in (3,) :
    print("spring")
elif Month in (4, 5) :
    print("spring")
elif Day >= 1 and Day <= 20 and Month in (6,) :
    print("spring")
elif Day >= 21 and Day <= 31 and Month in (6,) :
    print("summer")
elif Month in (7, 8) :
    print("summer")
elif Day >= 1 and Day <= 20 and Month in (9,) :
    print("summer")
elif Day >= 21 and Day <= 31 and Month  in (9,) :
    print("fall")
elif Month in (10, 11) :
    print("fall")
elif Day >= 1 and Day <= 20 and Month in (12,) :
    print("fall")





