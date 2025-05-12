import sys

D, H, M = map(int, sys.stdin.readline().split())

diff_day = D - 11
diff_hour = H - 11
diff_min = M - 11

if diff_min < 0:
    diff_hour -= 1
    diff_min += 60

if diff_hour < 0:
    diff_day -= 1
    diff_hour += 24

total = diff_day * 24 * 60 + diff_hour * 60 + diff_min

print(-1 if total < 0 else total)
