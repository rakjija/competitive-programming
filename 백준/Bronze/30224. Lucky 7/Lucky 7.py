import sys

N = sys.stdin.readline().rstrip("\n")

result = 0

if "7" in N:
    result = 2

if int(N) % 7 == 0:
    result += 1

print(result)
