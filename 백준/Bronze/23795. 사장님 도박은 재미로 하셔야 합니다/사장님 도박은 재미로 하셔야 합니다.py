import sys

total = 0
while True:
    money = int(sys.stdin.readline())

    if money == -1:
        break

    total += money

print(total)
