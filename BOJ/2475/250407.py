nums = map(int, input().split(" "))

sum = 0
for num in nums:
    sum += num**2

result = sum % 10
print(result)
