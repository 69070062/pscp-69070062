"""Impostor"""

import ast


def main():
    """Impostor"""
    people = {}
    while True:
        line = input().strip()
        if line == "Start":
            break
        d = ast.literal_eval(line)
        for k, v in d.items():
            people[k] = v

    dead = set()
    while True:
        line = input().strip()
        if line == "End":
            break
        dead.add(line)

    remain = 0
    for k, v in people.items():
        if k not in dead and v == "Impostor":
            remain += 1

    print(str(remain) + " Impostor Remains")
    print("***Alive***")
    for k, v in sorted(people.items()):
        if k not in dead:
            print(f"{k} : {v}")

    print("***Dead***")
    for k, v in sorted(people.items()):
        if k in dead:
            print(f"{k} : {v}")


if __name__ == "__main__":
    main()
