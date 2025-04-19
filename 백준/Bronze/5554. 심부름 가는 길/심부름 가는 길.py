import sys

total_sec = 0
for _ in range(4):
    total_sec += int(sys.stdin.readline())

print(total_sec // 60)
print(total_sec % 60)
