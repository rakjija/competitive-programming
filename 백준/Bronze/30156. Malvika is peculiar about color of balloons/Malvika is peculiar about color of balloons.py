import sys

t = int(sys.stdin.readline())


for _ in range(t):
    balloons = sys.stdin.readline().strip()

    print(min(balloons.count("a"), balloons.count("b")))
