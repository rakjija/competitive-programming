T = int(input())

result_list = []
for i in range(T):
    result = 0
    for correct in [str for str in input().split("X") if str != ""]:
        result += sum([(i + 1) for i, _ in enumerate(correct)])
    result_list.append(result)
print(*result_list, sep="\n")
