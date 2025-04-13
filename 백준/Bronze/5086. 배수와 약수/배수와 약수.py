import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0:
        break

    result = "neither"
    if A % B == 0:
        result = "multiple"
    if B % A == 0:
        result = "factor"

    print(result)
