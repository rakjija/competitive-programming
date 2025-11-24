import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

hamming_dist = 0
for i in range(n):
    if s[i] != t[i]:
        hamming_dist += 1

print(hamming_dist)
