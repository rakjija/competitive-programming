import sys

n = int(sys.stdin.readline())
weathers = list(map(int, sys.stdin.readline().split()))

total = 0
anger = 0
for w in weathers:
    anger += 1 if w == 1 else -1
    total += anger

print(total)
