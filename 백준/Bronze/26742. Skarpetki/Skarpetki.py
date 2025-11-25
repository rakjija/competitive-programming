import sys

socks = sys.stdin.readline().strip()
pair = {"B": 0, "C": 0}

for sock in socks:
    pair[sock] += 1

print(sum([count // 2 for count in pair.values()]))
