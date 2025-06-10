import sys

N = int(sys.stdin.readline())
As = list(map(int, sys.stdin.readline().split()))
Bs = list(map(int, sys.stdin.readline().split()))

result = 0
for i in range(N):
    if As[i] <= Bs[i]:
        result += 1

print(result)
