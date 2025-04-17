import sys

N = int(sys.stdin.readline().strip())

for i in range(1, N + 1):
    content = sys.stdin.readline().rstrip("\n")
    print(f"{i}. {content}")
