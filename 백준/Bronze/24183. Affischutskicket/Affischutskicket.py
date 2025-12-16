import sys

a, b, c = map(int, sys.stdin.readline().split())

envelope_weight = a * (0.229 * 0.324) * 2
poster_weight = b * (0.297 * 0.42) * 2
info_weight = c * (0.21 * 0.297)

total = envelope_weight + poster_weight + info_weight
print(f"{total:.6f}")
