import sys

while True:
    N = int(sys.stdin.readline().strip())
    if N == 0:
        break
    print(int(N * (N + 1) / 2))
