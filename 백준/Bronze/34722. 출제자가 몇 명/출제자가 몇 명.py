import sys

n = int(sys.stdin.readline())

total = 0
for _ in range(n):
    s, c, a, r = map(int, sys.stdin.readline().split())

    if s >= 1000:
        total += 1
        continue
    if c >= 1600:
        total += 1
        continue
    if a >= 1500:
        total += 1
        continue
    if r != -1 and r <= 30:
        total += 1
        continue

print(total)
