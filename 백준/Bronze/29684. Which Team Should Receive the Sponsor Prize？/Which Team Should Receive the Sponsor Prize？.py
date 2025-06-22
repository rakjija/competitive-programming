import sys

while True:
    T = int(sys.stdin.readline())
    if T == 0:
        break

    secs = list(map(int, sys.stdin.readline().split()))

    winner = 0
    winner_sec = 10**4
    for i in range(len(secs)):
        diff = abs(2023 - secs[i])
        if winner_sec >= diff:
            winner_sec = diff
            winner = i

    print(winner + 1)
