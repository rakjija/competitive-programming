N = int(input())
numbers = list(map(int, input().split()))

if len(numbers) != N:
    raise Exception("Wrong length input!")

result = 0
for number in numbers:
    if number == 1:
        continue
    if number == 2:
        result += 1
        continue
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        result += 1

print(result)
