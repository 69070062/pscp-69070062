"""test_result"""

people = int(input())
score_list = []

while people > 0:
    score = input()
    score_list.append(int(score))
    people -= 1

print(max(score_list))
print(score_list.count(max(score_list)))
