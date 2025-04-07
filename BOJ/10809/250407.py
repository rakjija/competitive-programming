alphabet = [chr(i + 97) for i in range(26)]
value = [-1] * 26
result = dict(zip(alphabet, value))

S = input()
for i in range(len(S)):
    if result[S[i]] == -1:
        result[S[i]] = i
print(*result.values())
