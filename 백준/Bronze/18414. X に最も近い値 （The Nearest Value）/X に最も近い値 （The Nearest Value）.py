import math
import sys

x, l, r = map(int, sys.stdin.readline().split())

min_diff = math.inf
min_idx = 0
for i in range(l, r + 1):
    if min_diff > abs(x - i):
        min_diff = abs(x - i)
        min_idx = i

print(min_idx)
