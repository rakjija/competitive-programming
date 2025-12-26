import sys

a, b, c, d = map(int, sys.stdin.readline().split())

by_shuttle = a + b <= d
by_walk = c <= d

if not by_shuttle and not by_walk:
    print("T.T")
else:
    if not by_shuttle:
        print("Walk")
    elif not by_walk:
        print("Shuttle")
    else:
        print("~.~")
