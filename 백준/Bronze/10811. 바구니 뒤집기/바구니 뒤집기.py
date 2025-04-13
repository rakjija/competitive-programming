import sys

N, M = map(int, sys.stdin.readline().split())

basket = [i + 1 for i in range(N)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    result = basket[i - 1 : j]
    result.reverse()
    basket[i - 1 : j] = result

print(*basket)
