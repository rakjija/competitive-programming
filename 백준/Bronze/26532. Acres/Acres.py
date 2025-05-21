import sys

x, y = map(int, sys.stdin.readline().split())

acre = x * y / 4840
result = int(acre // 5)
if acre % 5 != 0:
    result += 1

print(result)
