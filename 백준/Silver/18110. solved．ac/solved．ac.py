import sys


def round_up(n):
    if (n - int(n)) >= 0.5:
        return int(n) + 1
    else:
        return int(n)


n = int(sys.stdin.readline())

if n == 0:
    print(0)
else:
    difficulties = sorted([int(sys.stdin.readline()) for _ in range(n)])
    cut = round_up(n * 0.15)
    trimmed = difficulties[cut : n - cut]
    if len(trimmed) == 0:
        print(0)
    else:
        print(round_up(sum(trimmed) / len(trimmed)))
