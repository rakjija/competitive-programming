import sys

S = sys.stdin.readline().rstrip("\n")

if len(S) == 4:
    print(int(S[:2]) + int(S[2:]))
elif len(S) == 3:
    if S.startswith("10"):
        print(int(S[:2]) + int(S[-1]))
    else:
        print(int(S[0]) + int(S[1:]))
else:
    print(int(S[0]) + int(S[1]))
