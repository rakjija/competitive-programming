N = int(input())
numbers = list(map(int, input().split()))
if len(numbers) != N:
    raise Exception
v = int(input())
print(numbers.count(v))
