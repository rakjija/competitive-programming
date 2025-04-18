import sys

n = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
if len(S) != n:
    raise ValueError

nickname = []
for c in S:
    if c >= "A" and c <= "Z":
        nickname.append(c.lower())
    if c >= "a" and c <= "z":
        nickname.append(c.upper())

print("".join(nickname))
