import sys

for _ in range(2):
    T, F, S, P, C = map(int, sys.stdin.readline().split())

    print((T * 6) + (F * 3) + (S * 2) + (P * 1) + (C * 2))
