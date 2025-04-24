import sys

A = int(sys.stdin.readline().rstrip("\n"))
B = int(sys.stdin.readline().rstrip("\n"))
C = int(sys.stdin.readline().rstrip("\n"))
D = int(sys.stdin.readline().rstrip("\n"))
E = int(sys.stdin.readline().rstrip("\n"))

total = 0
if A < 0:
    total += abs(A) * C
    total += D
else:
    B -= A
total += B * E

print(total)
