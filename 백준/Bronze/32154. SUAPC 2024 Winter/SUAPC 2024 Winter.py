import sys

score = [chr(i + ord("A")) for i in range(13)]

N = int(sys.stdin.readline().rstrip("\n"))


if N not in {1, 4, 10}:
    score.remove("B")

if N not in {1}:
    score.remove("D")

if N in {10}:
    score.remove("E")

if N not in {2, 3}:
    score.remove("I")

if N not in {1}:
    score.remove("J")

score.remove("K")

print(len(score))
print(*score)
