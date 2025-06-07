import sys

N = int(sys.stdin.readline())
Ps = list(map(int, sys.stdin.readline().split()))
Ps.sort()

total = 0
for i, P in enumerate(Ps):
    total += P * (N - i)
print(total)
