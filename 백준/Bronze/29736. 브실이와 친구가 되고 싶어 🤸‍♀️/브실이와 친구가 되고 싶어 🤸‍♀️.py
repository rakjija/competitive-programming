import sys

A, B = map(int, sys.stdin.readline().split())
K, X = map(int, sys.stdin.readline().split())

total = 0
for i in range(A, B + 1):
    if abs(K - i) <= X:
        total += 1

print("IMPOSSIBLE" if total == 0 else total)
