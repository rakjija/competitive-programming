[hour, min] = map(int, input().split(" "))
required_min = int(input())

min += required_min
if min >= 60:
    min_to_hour = min // 60
    min -= 60 * min_to_hour
    hour += min_to_hour
    if hour > 23:
        hour -= 24

result = f"{hour} {min}"
print(result)
