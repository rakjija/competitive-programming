import sys

M, K = map(int, sys.stdin.readline().split())

print("No" if M % K != 0 else "Yes")
