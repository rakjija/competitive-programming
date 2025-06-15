import sys

fruits = ["Watermelon", "Pomegranates", "Nuts"]

b = int(sys.stdin.readline())

result = "Nothing"
for i in range(3):
    price = int(sys.stdin.readline())
    if b >= price:
        result = fruits[i]
        break

print(result)
