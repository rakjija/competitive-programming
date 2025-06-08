import sys

n = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip("\n")

result = 0
hidden = ""
for i in range(n):
    if (S[i] >= "a" and S[i] <= "z") or (S[i] >= "A" and S[i] <= "Z"):
        if len(hidden) > 0:
            result += int(hidden)
        hidden = ""
        continue

    hidden += S[i]

    if i == n - 1:
        if len(hidden) > 0:
            result += int(hidden)

print(result)
