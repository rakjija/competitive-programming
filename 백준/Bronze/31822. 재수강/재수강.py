import sys

S = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())

count = 0
for _ in range(N):
    T = sys.stdin.readline().rstrip()
    if S[:5] == T[:5]:
        count += 1

print(count)
