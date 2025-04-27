import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

if A > B:
    print(1)
elif A < B:
    print(-1)
else:
    print(0)
