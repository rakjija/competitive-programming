import sys

m = list(map(int, sys.stdin.readline().split()))

n = int(sys.stdin.readline().strip())

total = 0
for _ in range(n):
    b, l, s = sys.stdin.readline().split()
    b, l, s = int(b), float(l), int(s)

    if s >= 17 and l >= 2.0:
        total += m[int(b)]

print(total)
