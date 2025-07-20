import sys

N = sys.stdin.readline().strip()
print(bin(int(N, 8))[2:])
