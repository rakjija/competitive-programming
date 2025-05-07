import sys

E = sys.stdin.readline().rstrip("\n")

result = len(E)
for c in E:
    if c == ":":
        result += 1
    if c == "_":
        result += 5

print(result)
