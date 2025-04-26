import sys

n = int(sys.stdin.readline().rstrip("\n"))

total = 0
for _ in range(n):
    total += int(sys.stdin.readline().rstrip("\n"))

print(total)
