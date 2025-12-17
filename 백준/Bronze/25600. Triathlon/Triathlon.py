import sys

n = int(sys.stdin.readline())

max = 0

for _ in range(n):
    a, d, g = map(int, sys.stdin.readline().split())
    score = a * (d + g)
    if a == d + g:
        score += score

    if max < score:
        max = score

print(max)
