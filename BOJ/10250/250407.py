T = int(input())


result = []
for _ in range(T):
    [H, W, N] = map(int, input().split(" "))
    order = []

    for i in range(1, W + 1):
        for j in range(1, H + 1):
            X = j
            Y = i
            order.append(f"{X}{Y:02}")
    result.append(order[N - 1])

print("\n".join(result))
