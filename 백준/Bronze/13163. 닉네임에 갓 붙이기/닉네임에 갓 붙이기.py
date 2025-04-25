import sys

N = int(sys.stdin.readline().rstrip("\n"))

for _ in range(N):
    split_nickname = sys.stdin.readline().split()
    split_nickname[0] = "god"
    print("".join(split_nickname))
