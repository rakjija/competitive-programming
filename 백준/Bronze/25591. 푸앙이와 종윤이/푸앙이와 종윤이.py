import sys

x, y = map(int, sys.stdin.readline().split())

a = 100 - x
b = 100 - y
c = 100 - (a + b)
d = a * b
q = d // 100
r = d % 100
front = c + q
rear = r

print(a, b, c, d, q, r)
print(front, rear)
