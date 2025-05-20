import sys

pos = 1
neg = 1

N, A, B = map(int, sys.stdin.readline().split())

for _ in range(N):
    pos += A
    neg += B

    if pos < neg:
        temp = pos
        pos = neg
        neg = temp
    elif pos == neg:
        neg -= 1

print(pos, neg)
