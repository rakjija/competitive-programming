import sys

max = 0
for _ in range(2):
    total = sum(list(map(int, sys.stdin.readline().split())))
    if max < total:
        max = total

print(max)
