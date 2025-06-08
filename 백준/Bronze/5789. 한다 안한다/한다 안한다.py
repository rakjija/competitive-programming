import sys

N = int(sys.stdin.readline())
for _ in range(N):
    S = sys.stdin.readline().rstrip("\n")
    if S[len(S) // 2 - 1] == S[len(S) // 2]:
        print("Do-it")
    else:
        print("Do-it-Not")
