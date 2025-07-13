import sys

rotatable_letters = {"I", "O", "S", "H", "Z", "X", "N"}

S = sys.stdin.readline().strip()
result = "YES"
for letter in S:
    if letter not in rotatable_letters:
        result = "NO"
        break
print(result)
