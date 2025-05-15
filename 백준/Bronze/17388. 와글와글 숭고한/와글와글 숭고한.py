import sys

univs = ["Soongsil", "Korea", "Hanyang"]
scores = list(map(int, sys.stdin.readline().split()))

if sum(scores) >= 100:
    print("OK")
else:
    print(univs[scores.index(min(scores))])
