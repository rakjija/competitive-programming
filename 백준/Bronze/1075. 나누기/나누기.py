import sys

N = int(sys.stdin.readline().rstrip("\n"))
F = int(sys.stdin.readline().rstrip("\n"))

print(f"{(int(str(N)[-2:]) - (N % F)) % F:02d}")
