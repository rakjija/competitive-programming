import sys

N, M, K = map(int, sys.stdin.readline().split())

count = 0
count += min(M, K)
count += min(N - M, N - K)

print(count)
