import sys

X = int(sys.stdin.readline())
Y = int(sys.stdin.readline())

for y in range(X, Y + 1, 60):
    print(f"All positions change in year {y}")
