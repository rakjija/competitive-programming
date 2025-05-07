import sys

N = int(sys.stdin.readline())

result = [str(i) for i in range(1, N + 1)]

for i in range(0, N, 6):
    if i == 0:
        continue
    result.insert(i + (i // 6 - 1), "Go!")
result.append("Go!")

print(*result)
