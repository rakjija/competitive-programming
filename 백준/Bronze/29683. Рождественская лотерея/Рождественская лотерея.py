import sys

n, a = map(int, sys.stdin.readline().split())

a_list = list(map(int, sys.stdin.readline().split()))

total = 0
for i in range(n):
    total += a_list[i] // a

print(total)
