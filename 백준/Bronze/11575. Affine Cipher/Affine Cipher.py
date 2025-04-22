import sys

T = int(sys.stdin.readline().rstrip("\n"))

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().rstrip("\n")

    result = []
    for c in s:
        result.append(chr(((a * (ord(c) - ord("A")) + b) % 26) + ord("A")))

    print("".join(result))
