import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

v, h = 0, 0
for i in range(n):
    if s[i] == "N":
        v += 1
    elif s[i] == "S":
        v -= 1
    elif s[i] == "E":
        h += 1
    elif s[i] == "W":
        h -= 1

print(abs(v) + abs(h))
