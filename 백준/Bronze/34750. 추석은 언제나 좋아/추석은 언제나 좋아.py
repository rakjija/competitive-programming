import sys

n = int(sys.stdin.readline())

give = 0
if n >= 1_000_000:
    give = int(n * 0.2)
elif n >= 500_000:
    give = int(n * 0.15)
elif n >= 100_000:
    give = int(n * 0.1)
elif n < 100_000:
    give = int(n * 0.05)

print(give, n - give)
