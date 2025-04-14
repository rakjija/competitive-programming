import sys


def solution(L, x):
    answer = -1

    lower = 0
    upper = len(L) - 1
    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] > x:
            upper = middle - 1
        elif L[middle] < x:
            lower = middle + 1
        else:
            answer = middle
            break

    return answer


L = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline().strip())

print(solution(L, x))
