import sys

alphabet = [0] * 26

S = sys.stdin.readline().rstrip("\n")

for c in S:
    alphabet[ord(c) - ord("a")] += 1

print(*alphabet)
