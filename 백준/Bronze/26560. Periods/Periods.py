import sys

n = int(sys.stdin.readline())
for _ in range(n):
    s = sys.stdin.readline().rstrip("\n")
    if s[-1] != ".":
        s += "."
    print(s)
