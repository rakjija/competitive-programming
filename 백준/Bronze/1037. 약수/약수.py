import sys

N = int(sys.stdin.readline().rstrip("\n"))
divisors = list(map(int, sys.stdin.readline().split()))
if len(divisors) != N:
    raise ValueError

divisors.sort()

print(divisors[0] * divisors[-1])
