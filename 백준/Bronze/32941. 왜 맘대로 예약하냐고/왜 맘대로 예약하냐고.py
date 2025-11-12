import sys

t, x = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

flags = [0] * (t + 1)
for i in range(n):
    k = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    for j in range(k):
        flags[a[j]] += 1

if flags[x] == n:
    print("YES")
else:
    print("NO")
