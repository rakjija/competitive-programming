import sys

while True:
    n = int(sys.stdin.readline())

    # EE
    if n == 0:
        break

    result = 0
    for i in range(n):
        result += pow(i + 1, 3)

    print(result)
