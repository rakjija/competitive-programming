import sys

H = int(sys.stdin.readline())
W = int(sys.stdin.readline())

base = H if H < W else W
print(int(base * 100 / 2))
