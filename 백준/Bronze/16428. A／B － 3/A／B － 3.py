import sys

A, B = map(int, sys.stdin.readline().split())
q = abs(A) // abs(B)
r = abs(A) % abs(B)

if A < 0:
    q += 1
    q = -q
    r += 1

if B < 0:
    q = -q

print(q)
print(r)
