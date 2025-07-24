import sys

n: int = int(sys.stdin.readline().strip())
origin: str = sys.stdin.readline().strip()
rewrite: str = sys.stdin.readline().strip()

count = 0
for i in range(n):
    if origin[i] == rewrite[i]:
        count += 1

print(count)
