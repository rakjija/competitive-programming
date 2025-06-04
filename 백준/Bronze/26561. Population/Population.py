import sys

n = int(sys.stdin.readline())

for _ in range(n):
    p, t = map(int, sys.stdin.readline().split())

    p -= t // 7
    p += t // 4

    print(p)
