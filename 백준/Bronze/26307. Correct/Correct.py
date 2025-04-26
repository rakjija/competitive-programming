import sys

H, M = map(int, sys.stdin.readline().split())

print((H * 60 + M) - (9 * 60))
