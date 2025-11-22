import sys

m, d = map(int, sys.stdin.readline().split())

i = 0
while True:
    i += 1
    if m * i >= d:
        break

print(i)
