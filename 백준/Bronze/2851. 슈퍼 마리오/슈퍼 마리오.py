import sys

mushrooms = []
for _ in range(10):
    mushrooms.append(int(sys.stdin.readline()))

total = 0
for mushroom in mushrooms:
    if total + mushroom > 100:
        if 100 - total < total + mushroom - 100:
            break
    total += mushroom

print(total)
