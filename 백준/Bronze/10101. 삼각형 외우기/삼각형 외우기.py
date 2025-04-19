import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())
z = int(sys.stdin.readline())

if x + y + z == 180:
    if x == y and y == z and z == x:
        print("Equilateral")
    elif x != y and y != z and z != x:
        print("Scalene")
    else:
        print("Isosceles")
else:
    print("Error")
