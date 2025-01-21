rest_list = []
for _ in range(10):
    n = int(input())
    rest = n % 42
    if rest not in rest_list:
        rest_list.append(rest)
print(len(rest_list))
