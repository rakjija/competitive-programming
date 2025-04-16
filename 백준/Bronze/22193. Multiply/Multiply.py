import sys

N, M = map(int, sys.stdin.readline().split())

A = int(sys.stdin.readline().strip())
if len(str(A)) != N:
    raise Exception

B = int(sys.stdin.readline().strip())
if len(str(B)) != M:
    raise Exception

print(A * B)
