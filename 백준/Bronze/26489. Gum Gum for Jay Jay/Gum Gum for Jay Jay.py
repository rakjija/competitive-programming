import sys

count = 0
while True:
    line = sys.stdin.readline()
    if not line:
        break
    count += 1

print(count)
