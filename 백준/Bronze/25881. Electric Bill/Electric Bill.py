import sys

x, y = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

for _ in range(n):
    usage = int(sys.stdin.readline())

    cost = 0

    if usage <= 1000:
        cost += usage * x
    else:
        cost += 1000 * x
        cost += (usage - 1000) * y

    print(usage, cost)
