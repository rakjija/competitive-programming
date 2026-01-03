import sys

total = 0
for _ in range(4):
    parts = sys.stdin.readline().split()
    type = str(parts[0].strip())
    count = int(parts[1])

    if type == "Es":
        total += count * 21
    elif type == "Stair":
        total += count * 17
print(total)
