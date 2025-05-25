import sys

N = int(sys.stdin.readline())

print("Yes" if N <= 100000 and N % 2024 == 0 else "No")
