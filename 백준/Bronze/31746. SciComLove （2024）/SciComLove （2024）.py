import sys

N = int(sys.stdin.readline())
S = "SciComLove"

if N % 2 == 0:
  print(S)
else:
  print(S[::-1])
