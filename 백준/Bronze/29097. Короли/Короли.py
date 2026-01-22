import sys

n, m, k, a, b, c = map(int, sys.stdin.readline().split())

j = n * a
r = m * b
s = k * c

max = max(j, r, s)
results = []

if max <= j:
    results.append("Joffrey")
if max <= r:
    results.append("Robb")
if max <= s:
    results.append("Stannis")

print(" ".join(results))
