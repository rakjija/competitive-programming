import sys

total = 0
for i, n in enumerate("9780921418"):
    if i % 2 == 0:
        total += int(n)
    else:
        total += int(n) * 3

for i in range(3):
    n = int(sys.stdin.readline())
    if i % 2 == 0:
        total += n
    else:
        total += n * 3

print(f"The 1-3-sum is {total}")
