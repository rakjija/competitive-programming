import sys

scores = list(map(int, sys.stdin.readline().split()))
scores.sort()
print(scores[2] + scores[1])
