import sys

n = int(sys.stdin.readline())

recent_y = 0
recent_major = ""
for _ in range(n):
    major, y = sys.stdin.readline().split()
    if int(y) >= recent_y:
        recent_y = int(y)
        recent_major = major

print(recent_major)
