import sys

N = int(sys.stdin.readline())
P = []
for _ in range(N):
    P.append(int(sys.stdin.readline()))

M = int(sys.stdin.readline())
result = 0
for _ in range(M):
    result += P[int(sys.stdin.readline()) - 1]

print(result)
