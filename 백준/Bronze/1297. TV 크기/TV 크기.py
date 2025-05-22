import sys

D, H, W = map(int, sys.stdin.readline().split())
x = (D**2 / (H**2 + W**2)) ** 0.5

print(int(H * x), int(W * x))
