import sys

a, b = map(int, sys.stdin.readline().split())

print(a * a * (a + b + 1))
