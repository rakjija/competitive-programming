import sys

S = sys.stdin.readline().rstrip("\n")

a = int(S.split(" ")[0])
b = int(S.split(" ")[2])
c = int(S.split(" ")[4])

print("YES" if a + b == c else "NO")
