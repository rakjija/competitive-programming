import sys

a = int(sys.stdin.readline())
x = int(sys.stdin.readline())
b = int(sys.stdin.readline())
y = int(sys.stdin.readline())
t = int(sys.stdin.readline())

option1 = a + (((t - 30 if t - 30 > 0 else 0) * x) * 21)
option2 = b + (((t - 45 if t - 45 > 0 else 0) * y) * 21)

print(option1, option2)
