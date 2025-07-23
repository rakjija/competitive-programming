import sys

dong = [1, 2, 3, 4] * 6

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

print(dong[A + B + C + D - 2])
