T = int(input())

result_list = []
for _ in range(T):
    [A, B] = map(int, input().split())
    result_list.append(str(A + B))

result = "\n".join(result_list)
print(result)
