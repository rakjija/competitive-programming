import sys

while True:
    N = sys.stdin.readline().rstrip("\n")
    if N == "0 0 0":
        break
    first, diff, part = map(int, N.split())

    if part < first and diff > 0:
        print("X")
    elif part > first and diff < 0:
        print("X")
    elif (part - first) % diff == 0:
        print((part - first) // diff + 1)
    else:
        print("X")
