T = int(input())

result = []
for _ in range(T):
    [R, S] = input().split(" ")
    P = ""
    for char in S:
        P += char * int(R)
    result.append(P)

print("\n".join(result))
