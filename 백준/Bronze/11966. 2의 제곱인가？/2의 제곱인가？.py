import sys

N = int(sys.stdin.readline())

ans = set([2**i for i in range(31)])

print(1 if N in ans else 0)
