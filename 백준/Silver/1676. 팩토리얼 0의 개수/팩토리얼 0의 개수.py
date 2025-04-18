import math
import sys

N = int(sys.stdin.readline())

N_fac_str = str(math.factorial(N))

count = 0
while N >= 5:
    N //= 5
    count += N

print(count)
