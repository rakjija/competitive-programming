import sys

d = int(sys.stdin.readline())
cars = list(map(int, sys.stdin.readline().split()))

v = 0
for car in cars:
    if d == car:
        v += 1

print(v)
