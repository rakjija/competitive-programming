import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    result = [["."] * n for _ in range(n)]
    for i in range(n):
        result[i][0] = "#"
        result[i][n - 1] = "#"
        if i < n // 2 + 1:
            result[i][i] = "#"
            result[i][n - i - 1] = "#"

    print("\n".join("".join(row) for row in result))
