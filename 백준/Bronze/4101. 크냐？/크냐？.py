import sys

while True:
    N = sys.stdin.readline().strip()
    if N == "0 0":
        break
    A, B = map(int, N.split())
    print("Yes" if A > B else "No")
