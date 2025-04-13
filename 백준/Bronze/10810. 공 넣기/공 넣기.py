import sys

N, M = map(int, sys.stdin.readline().split())
basket = [0] * N
for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for index in range(i, j + 1):
        basket[index - 1] = k
print(*basket)
