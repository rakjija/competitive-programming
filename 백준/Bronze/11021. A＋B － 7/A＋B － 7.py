import sys

T = int(input())

result = []
for i in range(T):
    [A, B] = map(int, sys.stdin.readline().strip().split())
    result.append(f"Case #{i + 1}: {A + B}")

print(*result, sep="\n")
