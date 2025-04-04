[d1, d2, d3] = map(int, input().split(" "))

if d1 == d2 and d1 == d3 and d3 == d1:
    result = 10000 + d1 * 1000
elif d1 != d2 and d2 != d3 and d3 != d1:
    max = d1
    if max < d2:
        max = d2
    if max < d3:
        max = d3
    result = max * 100
else:
    target = 0
    if d1 == d2:
        target = d1
    if d2 == d3:
        target = d2
    if d3 == d1:
        target = d3
    result = 1000 + target * 100

print(result)
