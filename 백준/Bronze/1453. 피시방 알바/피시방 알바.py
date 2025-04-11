import sys

N = int(sys.stdin.readline().strip())
S = list(map(int, sys.stdin.readline().split()))
if len(S) != N:
    raise Exception

seated = set()
reject = 0

for s in S:
    if s in seated:
        reject += 1
    else:
        seated.add(s)

print(reject)
