import sys

n = int(sys.stdin.readline().strip())
garbages = list(map(int, sys.stdin.readline().split(" ")))

min_garbage = 0
min_i = 0
for i in range(n):
    if i == 0 or min_garbage > garbages[i]:
        min_garbage = garbages[i]
        min_i = i

print(min_i)
