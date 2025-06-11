import sys

T = int(sys.stdin.readline())
answers = map(int, sys.stdin.readline().split())

total = 0
for a in answers:
    if a == T:
        total += 1
print(total)
