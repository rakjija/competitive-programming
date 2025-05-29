import sys

x, y = map(int, sys.stdin.readline().split())

min = min(x, y)
max = max(x, y)

gcd = None
for i in range(1, min + 1):
    if max % i == 0 and min % i == 0:
        gcd = i
print(gcd)

lcm = None
i = 1
while True:
    if min * i % max == 0:
        lcm = min * i
        break
    i += 1
print(lcm)
