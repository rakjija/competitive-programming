import sys

N = int(sys.stdin.readline().strip())

for _ in range(N):
    P = sys.stdin.readline().strip()
    if len(P) >= 6 and len(P) <= 9:
        print("yes")
    else:
        print("no")
