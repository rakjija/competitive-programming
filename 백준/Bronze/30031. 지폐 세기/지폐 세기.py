import sys

n = int(sys.stdin.readline())

total = 0
for _ in range(n):
    w, h = map(int, sys.stdin.readline().split())
    if w == 136:
        total += 1000
    elif w == 142:
        total += 5000
    elif w == 148:
        total += 10000
    elif w == 154:
        total += 50000

print(total)
