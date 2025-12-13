import sys

a, b, c = map(int, sys.stdin.readline().split())

if abs(a - b) == c or abs(b - c) == a or abs(c - a) == b:
    print(1)
elif a * b == c or b * c == a or c * a == b:
    print(2)
else:
    print(3)
