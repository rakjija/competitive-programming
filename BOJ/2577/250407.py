A = int(input())
B = int(input())
C = int(input())

numbers = list(map(int, str(A * B * C)))
result = [0] * 10
for number in numbers:
    result[number] += 1

print(*result, sep="\n")

"""
한 번 틀림
0~9라서 [0] * 10 해야하는데
[0] * 9 라고 입력해서 틀림..
"""
