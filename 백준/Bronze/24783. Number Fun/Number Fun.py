import sys

N = int(sys.stdin.readline())

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())

    if a + b == c:
        print("Possible")
        continue

    if a - b == c or b - a == c:
        print("Possible")
        continue

    if a * b == c:
        print("Possible")
        continue

    if a / b == c or b / a == c:
        print("Possible")
        continue

    print("Impossible")
