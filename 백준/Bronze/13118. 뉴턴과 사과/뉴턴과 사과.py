import sys

ps = list(map(int, sys.stdin.readline().split()))
x, y, r = map(int, sys.stdin.readline().split())

crash = 0
for i, p in enumerate(ps):
    if x == p:
        crash = i + 1

print(crash)
