import sys

A, B, C = map(int, sys.stdin.readline().split())

if C == (A + B):
    print("correct!")
else:
    print("wrong!")
