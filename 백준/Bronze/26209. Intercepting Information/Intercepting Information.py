import sys

N = list(map(int, sys.stdin.readline().split()))

result = "S"
for n in N:
    if not (n == 0 or n == 1):
        result = "F"
        break

print(result)
