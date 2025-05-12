import sys

origin = "SciComLove"
S = sys.stdin.readline().rstrip("\n")

diff = 0
for i in range(len(origin)):
    if origin[i] != S[i]:
        diff += 1

print(diff)
