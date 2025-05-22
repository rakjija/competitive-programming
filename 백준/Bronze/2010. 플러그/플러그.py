import sys

N = int(sys.stdin.readline())

total = 0
for _ in range(N):
    total += int(sys.stdin.readline()) - 1
total += 1

print(total)
