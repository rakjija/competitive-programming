import sys

T = int(sys.stdin.readline())
for i in range(1, T + 1):
    x, y = map(int, sys.stdin.readline().split())
    print(f"Case {i}: {x + y}")
