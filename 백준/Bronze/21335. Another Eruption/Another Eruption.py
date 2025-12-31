import math
import sys

a = int(sys.stdin.readline())

r: float = math.sqrt(a / math.pi)

print(2 * math.pi * r)
