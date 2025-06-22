import sys

n = int(sys.stdin.readline())
for _ in range(n):
    p = int(sys.stdin.readline())
    max = 0
    result = ""
    for _ in range(p):
        C, name = sys.stdin.readline().split()
        if int(C) > max:
            max = int(C)
            result = name
    print(result)
