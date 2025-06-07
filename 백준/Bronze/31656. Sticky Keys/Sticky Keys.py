import sys

S = sys.stdin.readline().rstrip("\n")

result = ""
for c in S:
    if len(result) == 0 or result[-1] != c:
        result += c

print(result)
