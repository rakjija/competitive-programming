import sys

T = int(sys.stdin.readline().rstrip("\n"))

result = 0
for _ in range(T):
    n = int(sys.stdin.readline().rstrip("\n"))
    if n % 2 != 0:
        result += 1

print(result)
