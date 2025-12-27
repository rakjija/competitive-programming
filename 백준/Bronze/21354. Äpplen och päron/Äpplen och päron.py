import sys

a, p = map(int, sys.stdin.readline().split())

axel = a * 7
petra = p * 13

if axel > petra:
    print("Axel")
elif axel < petra:
    print("Petra")
else:
    print("lika")
