import sys

T = int(sys.stdin.readline())

for _ in range(T):
    x = int(sys.stdin.readline())

    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
