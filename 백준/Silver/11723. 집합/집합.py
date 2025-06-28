import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    N = sys.stdin.readline().rstrip("\n")
    if N == "all":
        S = set(range(1, 21))
        continue
    if N == "empty":
        S.clear()
        continue

    C, x = N.split()
    x = int(x)
    if C == "add":
        S.add(x)
        continue
    if C == "remove":
        S.discard(x)
        continue
    if C == "check":
        print(1 if x in S else 0)
        continue
    if C == "toggle":
        if x in S:
            S.remove(x)
        else:
            S.add(x)
        continue
