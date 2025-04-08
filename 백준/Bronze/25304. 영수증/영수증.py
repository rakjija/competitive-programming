import sys

X = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())

total = 0
for _ in range(N):
    [a, b] = map(int, sys.stdin.readline().strip().split())
    total += a * b

print("Yes" if total == X else "No")
