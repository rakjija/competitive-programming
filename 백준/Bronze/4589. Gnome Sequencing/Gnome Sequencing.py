import sys

N = int(sys.stdin.readline())

result = ["Gnomes:"]
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))

    if line == sorted(line) or line == sorted(line, reverse=True):
        result.append("Ordered")
    else:
        result.append("Unordered")

print(*result, sep="\n")
