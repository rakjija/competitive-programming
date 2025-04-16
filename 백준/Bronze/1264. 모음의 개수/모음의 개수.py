import sys

while True:
    S = sys.stdin.readline().strip()
    if S == "#":
        break

    total = 0
    for c in S:
        if c in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            total += 1

    print(total)
