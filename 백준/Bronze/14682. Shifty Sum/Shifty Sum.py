import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

result = 0
for i in range(k + 1):
    result += N * (10**i)

print(result)
