import sys

N, H = map(int, sys.stdin.readline().split())
A_list = list(map(int, sys.stdin.readline().split()))

available = 0
for i in range(N):
    if H >= A_list[i]:
        available += 1

print(available)
