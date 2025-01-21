result = []
for _ in range(10):
    n = int(input())
    rest = n % 42
    if rest not in result:
        result.append(rest)
print(len(result))
