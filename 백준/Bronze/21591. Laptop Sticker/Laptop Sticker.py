import sys

wc, hc, ws, hs = map(int, sys.stdin.readline().split())

is_fit = wc - ws >= 2 and hc - hs >= 2

print(1 if is_fit else 0)
