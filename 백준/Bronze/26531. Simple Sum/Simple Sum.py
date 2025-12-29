import sys

s = sys.stdin.readline().strip()

a = int(s.split("+")[0].strip())
b = int(s.split("+")[1].split("=")[0].strip())
c = int(s.split("=")[1].strip())

if a + b == c:
    print("YES")
else:
    print("NO")
