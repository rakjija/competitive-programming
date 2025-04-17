import sys

L = list(map(int, sys.stdin.readline().split()))

print(*list(sorted(L)))
