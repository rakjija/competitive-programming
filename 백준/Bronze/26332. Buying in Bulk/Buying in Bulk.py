import sys

n = int(sys.stdin.readline())

for _ in range(n):
    c, p = map(int, sys.stdin.readline().split())
    print(c, p)

    if c == 1:
        print(p)
    else:
        print((c * p) - ((c - 1) * 2))
