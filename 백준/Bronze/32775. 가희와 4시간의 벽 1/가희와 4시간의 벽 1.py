import sys

S = int(sys.stdin.readline().strip())
F = int(sys.stdin.readline().strip())

if S <= F:
    print("high speed rail")
else:
    print("flight")
