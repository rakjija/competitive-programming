import sys

while True:
    S = sys.stdin.readline().strip()
    if S == "# 0 0":
        break

    name, age, weight = S.split()
    age = int(age)
    weight = int(weight)

    part = "Junior"
    if age > 17 or weight >= 80:
        part = "Senior"

    print(f"{name} {part}")
