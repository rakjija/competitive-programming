import sys

L = int(sys.stdin.readline())

t = L // 5
if L % 5 != 0:
    t += 1

print(t)
