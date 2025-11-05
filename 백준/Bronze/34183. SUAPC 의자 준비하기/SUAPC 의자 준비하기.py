import sys

n, m, a, b = map(int, sys.stdin.readline().split())

need_chair = n * 3
chair = m

result = 0
if m < n * 3:
    result = ((need_chair - m) * a) + b

print(result)
