import sys

[A, B] = [int(number[::-1]) for number in sys.stdin.readline().split()]
print(B if A < B else A)
