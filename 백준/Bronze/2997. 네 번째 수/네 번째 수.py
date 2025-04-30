import sys

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
a, b, c = nums

if b - a < c - b:
    print(b + (b - a))
elif b - a > c - b:
    print(a + (c - b))
else:
    print(c + (b - a))
