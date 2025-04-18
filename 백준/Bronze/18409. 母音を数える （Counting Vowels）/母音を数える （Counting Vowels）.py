import sys

vowels = {"a", "e", "i", "o", "u"}

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
if len(S) != N:
    raise ValueError

vowel_count = 0
for c in S:
    if c in vowels:
        vowel_count += 1

print(vowel_count)
