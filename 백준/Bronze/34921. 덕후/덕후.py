import sys

a, t = map(int, sys.stdin.readline().split())

result = 10 + 2 * (25 - a + t)

print(0 if result < 0 else result)
