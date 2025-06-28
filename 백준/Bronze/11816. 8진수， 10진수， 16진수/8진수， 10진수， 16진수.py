import sys

X = sys.stdin.readline().rstrip("\n")

if X.startswith("0x"):
    result = int(X, 16)
elif X.startswith("0"):
    result = int(X, 8)
else:
    result = int(X)

print(result)
