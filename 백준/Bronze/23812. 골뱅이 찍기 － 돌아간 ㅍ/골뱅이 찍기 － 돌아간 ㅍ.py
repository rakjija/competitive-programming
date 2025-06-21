import sys

N = int(sys.stdin.readline())
result = []
for i in range(5):
    if i % 2 == 0:
        S = "@" * N + " " * (N * 3) + "@" * N
    if i % 2 == 1:
        S = "@" * (5 * N)
    for _ in range(N):
        result.append(S)

print("\n".join(result))
