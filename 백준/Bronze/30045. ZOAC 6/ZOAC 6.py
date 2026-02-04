import sys

n = int(sys.stdin.readline())

io_count = 0
for _ in range(n):
    s = sys.stdin.readline().strip()
    if "01" in s or "OI" in s:
        io_count += 1
print(io_count)
