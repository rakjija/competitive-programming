import sys

N = int(sys.stdin.readline())

result = 0
for _ in range(N):
    S = sys.stdin.readline().rstrip("\n")
    if S[0] == "C":
        result += 1

print(result)
