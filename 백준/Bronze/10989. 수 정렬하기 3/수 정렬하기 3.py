import sys

N = int(sys.stdin.readline().strip())

L = [0] * 10001
for _ in range(N):
    x = int(sys.stdin.readline().strip())
    L[x] += 1

for i in range(len(L)):
    if L[i] != 0:
        for _ in range(L[i]):
            print(i)
