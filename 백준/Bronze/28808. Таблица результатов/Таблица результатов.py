import sys

n, m = map(int, sys.stdin.readline().split())

solved = 0
for _ in range(n):
    p = sys.stdin.readline().strip()
    for i in range(m):
        if p[i] == "+":
            solved += 1
            break
        if p[i] == ".":
            break

print(solved)
