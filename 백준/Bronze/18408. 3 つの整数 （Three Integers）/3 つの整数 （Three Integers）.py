import sys

inputs = list(map(int, sys.stdin.readline().split()))

result = [0, 0, 0]
for input in inputs:
    result[input] += 1

for i in range(1, 3):
    if result[i] >= 2:
        print(i)
        break
