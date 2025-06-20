import sys

while True:
    S = sys.stdin.readline().rstrip("\n")
    if S == "0 0 0 0":
        break

    a, b, c, d = map(int, S.split())
    count = 0
    while True:
        if a == b == c == d:
            break
        count += 1
        temp = abs(a - b)
        b = abs(b - c)
        c = abs(c - d)
        d = abs(d - a)
        a = temp

    print(count)
