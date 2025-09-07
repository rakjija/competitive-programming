import sys

n = int(sys.stdin.readline())

qaly: float = 0.0
for _ in range(n):
    q, y = map(float, sys.stdin.readline().split())
    qaly += q * y

print(qaly)
