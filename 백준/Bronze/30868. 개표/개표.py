import sys

T = int(sys.stdin.readline().rstrip("\n"))

for _ in range(T):
    result = []
    N = int(sys.stdin.readline().rstrip("\n"))
    result = ["++++"] * (N // 5)
    result.append("".join(["|"] * (N % 5)))
    print(*result)
