import sys

n, k, a, b = map(int, sys.stdin.readline().split())

stair_sec = (n - 1) * a
elevator_sec = ((k - 1) + (n - 1)) * b

print(elevator_sec, stair_sec)
