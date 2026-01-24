import sys
from typing import cast

n = int(sys.stdin.readline())

gifticon_count = 0
for _ in range(n):
    s = cast(str, sys.stdin.readline().strip())
    d_day = int(s[2:])

    if d_day <= 90:
        gifticon_count += 1
print(gifticon_count)
