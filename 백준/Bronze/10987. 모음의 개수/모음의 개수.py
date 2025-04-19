import sys

vowels = {"a", "e", "i", "o", "u"}

S = sys.stdin.readline().rstrip("\n")

count = 0
for c in S:
    if c in vowels:
        count += 1

print(count)
