import sys

N = int(sys.stdin.readline().strip())

A = int(N * (N + 1) / 2)
B = int(N * (N + 1) / 2) ** 2
C = 0
for i in range(1, N + 1):
    C += i**3

print(A)
print(B)
print(C)
