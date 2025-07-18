import sys

n = int(sys.stdin.readline().strip())

result = [n]
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
    result.append(n)

print(*result)
