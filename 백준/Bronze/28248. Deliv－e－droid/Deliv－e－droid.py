import sys

P = int(sys.stdin.readline())
C = int(sys.stdin.readline())

score = P * 50 - C * 10
if P > C:
    score += 500
print(score)
