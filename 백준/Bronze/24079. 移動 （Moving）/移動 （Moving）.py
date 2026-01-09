import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())
z = int(sys.stdin.readline())

if x + y < z + 0.5:
    print(1)
else:
    print(0)
