import sys

while True:
    S = sys.stdin.readline().rstrip()
    if S == "0":
        break
    p = True
    for i in range(len(S) // 2):
        if S[i] != S[len(S) - i - 1]:
            p = False
            break
    print("yes" if p else "no")
