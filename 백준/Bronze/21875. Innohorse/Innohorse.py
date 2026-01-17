import sys
from typing import cast

start = cast(list[str], sys.stdin.readline().strip())
end = cast(list[str], sys.stdin.readline().strip())

xy = [
    abs(ord(start[0]) - ord(end[0])),
    abs(int(start[1]) - int(end[1])),
]
xy.sort()

print(xy[0], xy[1])
