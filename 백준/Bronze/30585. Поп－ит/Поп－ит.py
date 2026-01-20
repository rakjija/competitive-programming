import sys
from typing import cast

h, w = map(int, sys.stdin.readline().split())
total = h * w
count = 0
for _ in range(h):
    line = cast(str, sys.stdin.readline().strip())
    for i in range(w):
        if int(line[i]) == 1:
            count += 1
print(count if total / 2 > count else total - count)
