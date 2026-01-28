import sys

s = str(sys.stdin.readline().strip())

i = 0
result = []
while True:
    if i == 0:
        result.append(s[i])
    else:
        diff = ord(s[i - 1]) - ord("A")
        i += diff
        result.append(s[i])
    i += 1
    if i >= len(s):
        break

print("".join(result))
