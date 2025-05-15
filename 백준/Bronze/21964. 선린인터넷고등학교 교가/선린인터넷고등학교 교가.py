import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip("\n")
if N != len(S):
    raise ValueError

print(S[-5:])
