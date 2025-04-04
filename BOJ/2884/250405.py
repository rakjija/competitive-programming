[hour, minute] = map(int, input().split(" "))

if minute < 45:
    minute = 60 - (45 - minute)
    hour -= 1
    if hour < 0:
        hour = 23
else:
    minute -= 45

print(f"{hour} {minute}")
