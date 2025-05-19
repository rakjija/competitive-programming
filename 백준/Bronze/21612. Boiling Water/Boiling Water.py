import sys

B = int(sys.stdin.readline())

p = 5 * B - 400
print(p)

if p < 100:
    print(1)
elif p > 100:
    print(-1)
else:
    print(0)
