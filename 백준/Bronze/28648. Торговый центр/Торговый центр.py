import sys

n = int(sys.stdin.readline())

min = 200
for _ in range(n):
    t, l = map(int, sys.stdin.readline().split())
    if t + l < min:
        min = t + l
print(min)
