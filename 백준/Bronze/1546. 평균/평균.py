import sys

N = int(sys.stdin.readline().strip())
scores = list(map(int, sys.stdin.readline().strip().split()))
if len(scores) != N:
    raise Exception

M = 0
for score in scores:
    if M < score:
        M = score

result = []
for score in scores:
    result.append(score / M * 100)

print(sum(result) / len(result))
