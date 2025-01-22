count = int(input())

account_book = []
for _ in range(count):
    n = int(input())
    if n == 0:
        if len(account_book) != 0:
            account_book.pop()
    else:
        account_book.append(n)

sum = 0
for n in account_book:
    sum += n

print(sum)
