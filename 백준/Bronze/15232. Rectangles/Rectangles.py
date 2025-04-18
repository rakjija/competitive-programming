import sys

R = int(sys.stdin.readline())
C = int(sys.stdin.readline())

print(*["*" * C] * R, sep="\n")
