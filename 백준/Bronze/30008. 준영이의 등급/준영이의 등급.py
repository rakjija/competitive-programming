import sys

N, K = map(int, sys.stdin.readline().split())
Gs = list(map(int, sys.stdin.readline().split()))
if K != len(Gs):
    raise ValueError

for G in Gs:
    P = G * 100 // N

    if P >= 0 and P <= 4:
        print(1, end=" ")
    elif P > 4 and P <= 11:
        print(2, end=" ")
    elif P > 11 and P <= 23:
        print(3, end=" ")
    elif P > 23 and P <= 40:
        print(4, end=" ")
    elif P > 40 and P <= 60:
        print(5, end=" ")
    elif P > 60 and P <= 77:
        print(6, end=" ")
    elif P > 77 and P <= 89:
        print(7, end=" ")
    elif P > 89 and P <= 96:
        print(8, end=" ")
    elif P > 96 and P <= 100:
        print(9, end=" ")
