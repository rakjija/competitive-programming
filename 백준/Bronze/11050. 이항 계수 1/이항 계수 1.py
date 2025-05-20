import sys


def fac(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


N, K = map(int, sys.stdin.readline().split())

print(int(fac(N) / (fac(K) * fac(N - K))))
