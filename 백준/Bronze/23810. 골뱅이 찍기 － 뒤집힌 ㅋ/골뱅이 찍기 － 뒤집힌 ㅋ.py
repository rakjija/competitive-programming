import sys

N = int(sys.stdin.readline())

result = ""
for i in range(5):
    for j in range(N):
        if i == 0 or i == 2:
            result += "@@@@@" * N + "\n"
        else:
            result += "@" * N + "\n"
print(result)
