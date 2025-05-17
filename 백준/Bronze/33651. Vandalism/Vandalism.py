import sys

s = sys.stdin.readline().rstrip("\n")

letters = ["U", "A", "P", "C"]
for c in s:
    letters.remove(c)

print("".join(letters))
