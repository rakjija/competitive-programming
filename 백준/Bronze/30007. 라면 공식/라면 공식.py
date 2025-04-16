import sys

N = int(sys.stdin.readline().strip())

for _ in range(N):
    A, B, X = map(int, sys.stdin.readline().split())
    print(A * (X - 1) + B)
