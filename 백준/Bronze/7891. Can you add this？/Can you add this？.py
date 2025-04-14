import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    x, y = list(map(int, sys.stdin.readline().split()))
    print(x + y)
