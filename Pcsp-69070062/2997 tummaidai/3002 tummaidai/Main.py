"""paspas"""

first = input()
surname = input()
age = input()

if len(first) >= 5 and len(surname) >= 5:
    print(first[:2] + surname[-1] + age[-1])

else:
    print(first[0] + age + surname[-1])
