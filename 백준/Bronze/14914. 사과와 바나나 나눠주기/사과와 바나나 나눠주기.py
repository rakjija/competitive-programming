import sys

a, b = map(int, sys.stdin.readline().split())

minimum = min(a, b)

cd = []
for i in range(1, minimum + 1):
    if a % i == 0 and b % i == 0:
        cd.append(i)

for d in cd:
    print(d, a // d, b // d)
