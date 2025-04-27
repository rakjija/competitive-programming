import sys

n = int(sys.stdin.readline())
moves = list(map(int, sys.stdin.readline().split()))
if len(moves) != n:
    raise ValueError
if sum(moves) > 0:
    print("Right")
elif sum(moves) < 0:
    print("Left")
else:
    print("Stay")
