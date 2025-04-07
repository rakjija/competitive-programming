result_list = []
while True:
    [A, B] = map(int, input().split(" "))
    if A == 0 and B == 0:
        break
    result_list.append(A + B)
print("\n".join(map(str, result_list)))
