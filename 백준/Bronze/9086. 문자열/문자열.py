T = int(input())

result = []
for i in range(T):
    S = input()
    result.append(S[0] + S[-1])
print(*result, sep="\n")
