import sys

sec = 300
for _ in range(4):
    sec += int(sys.stdin.readline().strip())

print("Yes" if sec <= 1800 else "No")
