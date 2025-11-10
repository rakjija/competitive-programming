import sys

t = int(sys.stdin.readline())

for _ in range(t):
    c = sys.stdin.readline().strip()

    w = 0
    for i in range(len(c)):
        if c[i] == "U":
            w += 1
        if c[i] == "D":
            break

    print(w)
