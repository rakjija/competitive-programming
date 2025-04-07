result = [0] * 1000
for i in range(10):
    result[int(input()) % 42] = 1
print(sum(result))
