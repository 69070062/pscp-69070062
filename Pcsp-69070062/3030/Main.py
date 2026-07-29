"""Saitama"""

push = int(input())
sit = int(input())
luk = int(input())
run = int(input())
pushday = int(input())
sitday = int(input())
runday = int(input()) 
lukday = int(input())

days_push = 0
done = 0
while done < push:
    done += pushday
    days_push += 1
days_sit = 0
done = 0
while done < sit:
    done += sitday
    days_sit += 1
days_luk = 0
done = 0
while done < luk:
    done += lukday
    days_luk += 1
days_run = 0
done = 0
while done < run:
    done += runday
    days_run += 1

print(max(days_push, days_sit, days_luk, days_run))
