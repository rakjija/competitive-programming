import sys

N = int(sys.stdin.readline())
answers = map(int, sys.stdin.readline().split())

score = 0
total = 0
for answer in answers:
    if answer == 0:
        score = 0
    else:
        score += 1
        total += score

print(total)
