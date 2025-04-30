import sys

T = int(sys.stdin.readline())
N = int(sys.stdin.readline())
Fs = list(map(int, sys.stdin.readline().split()))
if N != len(Fs):
    raise ValueError

if T > sum(Fs):
    print("Padaeng_i Cry")
else:
    print("Padaeng_i Happy")
