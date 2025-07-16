import sys

A = list(map(int, sys.stdin.readline().split()))
R = list(map(int, sys.stdin.readline().split()))

result = 0
for i in range(3):
    if A[i] >= R[i]:
        continue
    else:
        result += R[i] - A[i]

print(result)
