import sys

N = int(sys.stdin.readline().strip())

A = int(N * (78 / 100))
B = int(N - (N * (20 / 100) * (22 / 100)))

print(A, B)
