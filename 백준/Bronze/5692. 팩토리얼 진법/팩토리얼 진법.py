import math
import sys

while True:
    N = sys.stdin.readline().strip()
    if N == "0":
        break

    result = 0
    for i in range(len(N)):
        result += int(N[i]) * math.factorial(len(N) - i)
    print(result)
