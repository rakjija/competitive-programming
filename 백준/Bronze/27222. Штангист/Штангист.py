import sys

n = int(sys.stdin.readline())
days = list(map(int, sys.stdin.readline().split()))

muscles = 0
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())

    if days[i] == 0:
        continue

    increase = y - x
    if increase > 0:
        muscles += increase

print(muscles)
