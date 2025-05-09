import sys

S = sys.stdin.readline().rstrip("\n")

result = []
for c in S:
    if c < "A" or c > "z":
        result.append(c)
        continue

    base = ord("a") if c >= "a" else ord("A")
    rot13 = ord(c) + 13
    if rot13 - base >= 26:
        rot13 -= 26

    result.append(chr(rot13))

print("".join(result))
