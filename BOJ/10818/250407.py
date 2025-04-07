N = int(input())
numbers = list(map(int, input().split(" ")))

if len(numbers) != N:
    raise Exception

max = float("-inf")
min = float("inf")

for number in numbers:
    if max < number:
        max = number
    if min > number:
        min = number

print(min, max)
