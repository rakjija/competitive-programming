import sys

a1, a2, a3 = map(int, sys.stdin.readline().split())
b1, b2, b3 = map(int, sys.stdin.readline().split())

t1 = a1 + 2 * a2 + 3 * a3
t2 = b1 + 2 * b2 + 3 * b3

if t1 > t2:
    print(1)
elif t1 < t2:
    print(2)
else:
    print(0)
