import sys

m = int(sys.stdin.readline())
d = int(sys.stdin.readline())

if m > 2:
    print("After")
elif m < 2:
    print("Before")
else:
    if d > 18:
        print("After")
    elif d < 18:
        print("Before")
    else:
        print("Special")
