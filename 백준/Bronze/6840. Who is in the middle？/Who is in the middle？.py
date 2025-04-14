import sys

bears = []
for _ in range(3):
    bears.append(int(sys.stdin.readline().strip()))
bears.sort()
print(bears[1])
