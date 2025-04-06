[N, K] = map(int, input().split(" "))

for _ in range(N):
    [A, B] = map(int, input().split(" "))
    K += A
    K -= B

print("비와이")
