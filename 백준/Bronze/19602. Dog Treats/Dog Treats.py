import sys

happy_point = 0
for i in range(1, 3 + 1):
    happy_point += i * int(sys.stdin.readline())

print("happy" if happy_point >= 10 else "sad")
