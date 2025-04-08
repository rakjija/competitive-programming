N = int(input())
N_numbers = set(map(int, input().split()))

M = int(input())
M_numbers = list(map(int, input().split()))
if len(M_numbers) != M:
    raise Exception

result = []
for number in M_numbers:
    if number in N_numbers:
        result.append(1)
    else:
        result.append(0)

print(*result, sep="\n")
