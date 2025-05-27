import sys

Z = int(sys.stdin.readline())

for _ in range(Z):
    W, K = map(int, sys.stdin.readline().split())
    print(W * K // 2)
