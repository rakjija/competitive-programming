import sys

T = int(sys.stdin.readline())

for i in range(1, T+1):
    sacks = map(int, sys.stdin.readline().split())
    print(f'Case #{i}: {max(sacks)}')