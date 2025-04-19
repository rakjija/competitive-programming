import sys

N = int(sys.stdin.readline().rstrip("\n"))

files = []
for i in range(N):
    files.append(sys.stdin.readline().rstrip("\n"))

result = []
for i in range(len(files[0])):
    char = ""
    for j in range(N):
        if j == 0:
            char = files[j][i]
            continue
        if char != files[j][i]:
            char = "?"
    result.append(char)

print("".join(result))
