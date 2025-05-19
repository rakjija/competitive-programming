import sys

prev = 201
while True:
    N = float(sys.stdin.readline())
    if N == 999:
        break

    if prev == 201:
        prev = N
        continue

    print(f"{N - prev:.2f}")
    prev = N
