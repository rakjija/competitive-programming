import sys

P, M = map(int, sys.stdin.readline().split())

A = (P + M) // 2
B = (P - M) // 2

if (P + M) % 2 != 0 or (P - M) % 2 != 0 or A < 0 or B < 0:
    print(-1)
else:
    print(max(A, B), min(A, B))
