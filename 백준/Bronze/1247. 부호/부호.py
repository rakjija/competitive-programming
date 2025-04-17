import sys

for _ in range(3):
    N = int(sys.stdin.readline().rstrip("\n"))

    L = []
    for _ in range(N):
        L.append(int(sys.stdin.readline().rstrip("\n")))
    total = sum(L)

    if total < 0:
        print("-")
    elif total > 0:
        print("+")
    else:
        print("0")
