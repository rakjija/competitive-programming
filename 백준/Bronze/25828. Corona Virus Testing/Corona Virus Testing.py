import sys

g, p, t = map(int, sys.stdin.readline().split())

g_count = g + (t * p)
p_count = g * p

if g_count < p_count:
    print(2)
elif g_count > p_count:
    print(1)
else:
    print(0)
