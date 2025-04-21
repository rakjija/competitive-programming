import sys

bottles = list(map(int, sys.stdin.readline().split()))

result = 0
for bottle in bottles:
    result += bottle * 5

print(result)
