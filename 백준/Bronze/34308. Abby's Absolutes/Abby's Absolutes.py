import sys

n, k = map(int, sys.stdin.readline().split())
needs = list(map(int, sys.stdin.readline().split()))

buys: list[str] = []
for i in range(k):
    if n - needs[i] >= needs[i] - 1:
        buys.append("1")
    elif n - needs[i] < needs[i] - 1:
        buys.append(str(n))

print(" ".join(buys))
