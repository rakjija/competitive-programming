import sys

X = int(input())
N = int(input())

price = []
for _ in range(N):
    [a, b] = map(int, sys.stdin.readline().split())
    price.append(a * b)

if sum(price) == X:
    print("Yes")
else:
    print("No")
