import sys

case = 1
while True:
    N, *numbers = list(map(int, sys.stdin.readline().split()))
    if N == 0:
        break
    if N != len(numbers):
        raise ValueError

    print(f"Case {case}: Sorting... done!")
    case += 1
