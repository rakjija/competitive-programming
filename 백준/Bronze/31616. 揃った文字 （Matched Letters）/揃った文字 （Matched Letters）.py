import sys

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

result = "Yes"
for i in range(1, n):
    if s[i] != s[i - 1]:
        result = "No"
        break

sys.stdout.write(result + "\n")
