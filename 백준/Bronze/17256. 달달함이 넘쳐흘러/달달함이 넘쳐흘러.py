import sys

ax, ay, az = map(int, sys.stdin.readline().split())
cx, cy, cz = map(int, sys.stdin.readline().split())

print(cx - az, int(cy / ay), cz - ax)
