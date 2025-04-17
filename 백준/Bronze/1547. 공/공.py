import sys

M = int(sys.stdin.readline())

pos = [0, 1, 0, 0]
for _ in range(M):
    X, Y = map(int, sys.stdin.readline().split())

    temp = pos[X]
    pos[X] = pos[Y]
    pos[Y] = temp

try:
    print(pos.index(1))
except ValueError:
    print(-1)
