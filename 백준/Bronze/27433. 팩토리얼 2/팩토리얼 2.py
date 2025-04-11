import sys

N = int(sys.stdin.readline().strip())

result = 1
if N != 0:
    for num in range(1, N + 1):
        result *= num
print(result)
