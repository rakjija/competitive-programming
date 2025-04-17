import sys

N = int(sys.stdin.readline().rstrip("\n"))
T = list(map(int, sys.stdin.readline().split()))
if len(T) != N:
    raise Exception

Y = 0
M = 0
for t in T:
    Y += (t // 30 + 1) * 10
    M += (t // 60 + 1) * 15


if M > Y:
    print(f"Y {Y}")
elif M < Y:
    print(f"M {M}")
else:
    print(f"Y M {Y}")
