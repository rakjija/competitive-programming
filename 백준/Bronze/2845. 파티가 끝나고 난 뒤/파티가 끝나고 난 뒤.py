import sys

P = list(map(int, sys.stdin.readline().split()))
if len(P) != 2:
    raise Exception

N = list(map(int, sys.stdin.readline().split()))
if len(N) != 5:
    raise Exception

area = P[0] * P[1]

result = []
for news_count in N:
    result.append(news_count - area)

print(*result)
