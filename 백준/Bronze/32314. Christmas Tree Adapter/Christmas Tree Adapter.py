import sys

a = int(sys.stdin.readline().rstrip("\n"))
w, v = map(int, sys.stdin.readline().split())

print(1 if a <= w / v else 0)
