import sys

N = int(sys.stdin.readline().rstrip("\n"))
candies = list(map(int, sys.stdin.readline().split()))
if len(candies) != N:
    raise ValueError

result = 0
odd_candies = [candy for candy in candies if candy % 2 != 0]
if len(odd_candies) % 2 == 0:
    result = sum(candies)
else:
    odd_candies.sort()
    result = sum(candies) - odd_candies[0]

print(result)
