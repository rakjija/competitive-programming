import sys

n = int(sys.stdin.readline())

can_make_seven = True
for _ in range(3):
    wheel_numbers = list(map(int, sys.stdin.readline().split()))[:n]
    if 7 not in wheel_numbers:
        can_make_seven = False

print(777 if can_make_seven else 0)
