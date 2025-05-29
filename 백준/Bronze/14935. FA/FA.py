import sys

S = sys.stdin.readline().rstrip("\n")

while True:
    n = int(S[0]) * len(S)
    if n == int(S):
        print("FA")
        break
    else:
        if len(S) == 1:
            print("NFA")
            break
        S = str(n)
