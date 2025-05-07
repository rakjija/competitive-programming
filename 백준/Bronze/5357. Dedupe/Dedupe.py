import sys

N = int(sys.stdin.readline())

for _ in range(N):
    S = sys.stdin.readline().rstrip()
    result = [S[0]]
    for i in range(1, len(S)):
        if S[i] != S[i - 1]:
            result.append(S[i])
    print("".join(result))
