import sys

n, m = map(int, sys.stdin.readline().split())

if n == m:
    print(n + m)
else:
    flag = min(n, m)
    print(flag * 2 + 1)
