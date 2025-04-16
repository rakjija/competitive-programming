import sys

T1, T2 = map(int, sys.stdin.readline().split())

if T1 < T2:
    print(T1)
else:
    print(T2)
