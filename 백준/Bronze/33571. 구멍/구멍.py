import sys

hole_exist = (
    "A",
    "a",
    "B",
    "b",
    "D",
    "d",
    "e",
    "g",
    "O",
    "o",
    "P",
    "p",
    "Q",
    "q",
    "R",
    "@",
)

S = sys.stdin.readline().rstrip("\n")

count = 0
for s in S:
    if s in hole_exist:
        count += 1
        if s == "B":
            count += 1

print(count)
