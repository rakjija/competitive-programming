import math
import sys

T = int(sys.stdin.readline())
for _ in range(1, T + 1):
    N = int(sys.stdin.readline())
    print(str(math.factorial(N))[-1])
