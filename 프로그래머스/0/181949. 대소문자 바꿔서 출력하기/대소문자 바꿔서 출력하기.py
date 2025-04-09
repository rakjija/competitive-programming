str = input()
result = []
for char in str:
    if char >= 'a' and char <= 'z':
        result.append(char.upper())
    elif char >= 'A' and char <= 'Z':
        result.append(char.lower())
print(''.join(result))