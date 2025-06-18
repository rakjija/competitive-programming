import math
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    A1, P1 = map(int, sys.stdin.readline().split())
    R1, P2 = map(int, sys.stdin.readline().split())

    slice = A1 / P1
    whole = (R1**2 * math.pi) / P2

    if slice < whole:
        print("Whole pizza")
    else:
        print("Slice of pizza")
