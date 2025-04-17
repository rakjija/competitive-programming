import sys

A, B, C = map(int, sys.stdin.readline().split())
T = int(sys.stdin.readline().strip())

fin_time = (A * 60 * 60) + (B * 60) + C + T
H = fin_time // (60 * 60) % 24
M = (fin_time // 60) % 60
S = fin_time % 60

print(H, M, S)
