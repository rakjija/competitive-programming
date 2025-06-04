import sys

N = int(sys.stdin.readline())

table = [1]
for i in range(2, 10):
    for j in range(1, 10):
        table.append(i * j)

print(1 if N in set(table) else 0)
