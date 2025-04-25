import sys

K, N, M = map(int, sys.stdin.readline().split())

print(K * N - M if K * N >= M else 0)
