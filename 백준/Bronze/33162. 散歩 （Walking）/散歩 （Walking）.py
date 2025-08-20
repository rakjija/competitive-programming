import sys

x = int(sys.stdin.readline().strip())

m = 0
for i in range(x):
    if i % 2 == 0:
        m += 3
    else:
        m -= 2
print(m)
