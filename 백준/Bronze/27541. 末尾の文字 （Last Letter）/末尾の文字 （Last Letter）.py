import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

if s[n - 1] == "G":
    print(s[:-1])
else:
    print(s + "G")
