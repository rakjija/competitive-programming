import sys

N = int(sys.stdin.readline())

result = [1001, 1001]
for i in range(N):
    station = list(map(int, sys.stdin.readline().split()))
    if result[1] > station[1]:
        result = station

print(*result)
