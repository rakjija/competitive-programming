import sys

x, n = map(int, sys.stdin.readline().split())

result = x
for _ in range(n):
    if result % 2 == 0:
        result = int(result / 2) ^ 6
    else:
        result = int(result * 2) ^ 6

print(result)
