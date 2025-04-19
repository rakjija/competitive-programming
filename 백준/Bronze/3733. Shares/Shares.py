import sys

while True:
    text = sys.stdin.readline().rstrip("\n")
    if text == "":
        break

    N, S = map(int, text.split())

    print(S // (N + 1))
