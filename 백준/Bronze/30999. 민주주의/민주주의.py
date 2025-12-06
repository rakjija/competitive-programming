import sys

n, m = map(int, sys.stdin.readline().split())

total = 0
for _ in range(n):
    s = sys.stdin.readline().strip()

    count = 0
    for i in range(m):
        if s[i] == "O":
            count += 1

    if count >= ((m // 2) + 1):
        total += 1

print(total)
