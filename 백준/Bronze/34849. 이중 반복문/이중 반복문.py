import math
import sys

n = int(sys.stdin.readline())

if int(math.pow(n, 2)) <= 100000000:
    print("Accepted")
else:
    print("Time limit exceeded")
