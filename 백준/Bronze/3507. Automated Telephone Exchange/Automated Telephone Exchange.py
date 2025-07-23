import sys

n: int = int(sys.stdin.readline().strip())

result: int = 99 - (n - 99) + 1

print(result if result > 0 else 0)
