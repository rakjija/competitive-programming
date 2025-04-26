import sys

A = int(sys.stdin.readline().rstrip("\n"))
B = int(sys.stdin.readline().rstrip("\n"))
C = int(sys.stdin.readline().rstrip("\n"))

print(1 if A + B + C <= 21 else 0)
