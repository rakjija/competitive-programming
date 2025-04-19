import sys

total = int(sys.stdin.readline())

book_9_price = 0
for _ in range(9):
    book_9_price += int(sys.stdin.readline())

print(total - book_9_price)
