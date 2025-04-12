import sys

J = sys.stdin.readline().strip()
D = sys.stdin.readline().strip()

if len(D) <= len(J):
    print("go")
else:
    print("no")
