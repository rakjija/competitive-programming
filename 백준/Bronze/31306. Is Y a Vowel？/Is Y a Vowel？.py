import sys

s = sys.stdin.readline().strip()

count = 0
count_y = 0
for c in s:
    if c in ["a", "e", "i", "o", "u"]:
        count += 1
    if c == "y":
        count_y += 1

print(count, count + count_y)
