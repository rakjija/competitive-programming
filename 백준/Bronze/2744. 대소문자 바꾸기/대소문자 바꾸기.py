S = input()
result = ""
for char in S:
    if char >= "A" and char <= "Z":
        result += char.lower()
    elif char >= "a" and char <= "z":
        result += char.upper()
print(result)
