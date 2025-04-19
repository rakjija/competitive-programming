import sys

X = int(sys.stdin.readline())
Y = int(sys.stdin.readline())

N = (X - Y) // 2
K = X - N

print(K)
print(N)
