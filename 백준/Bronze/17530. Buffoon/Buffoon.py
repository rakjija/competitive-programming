import sys

N = int(sys.stdin.readline())
temp = 0
result = "S"
for i in range(N):
    v = int(sys.stdin.readline())
    if result == "N":
        continue

    if i == 0:
        temp = v
    else:
        if temp < v:
            result = "N"

print(result)
