import sys

n, m = map(int, sys.stdin.readline().split())

isPass = True
for _ in range(n):
    ms = sys.stdin.readline().split()

    if not isPass:
        continue

    count_a = 0
    for i in range(m):
        if ms[i] == "A":
            count_a += 1

    if count_a == 0 or count_a > 1:
        isPass = False

print("Yes" if isPass else "No")
