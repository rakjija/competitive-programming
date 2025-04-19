import sys

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline().rstrip("\n"))

if A + B >= C * 2:
    print((A + B) - (C * 2))
else:
    print(A + B)
