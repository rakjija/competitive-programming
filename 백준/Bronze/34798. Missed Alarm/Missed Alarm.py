import sys

alarm_h, alarm_m = map(int, sys.stdin.readline().split(":"))
watch_h, watch_m = map(int, sys.stdin.readline().split(":"))

if alarm_h < watch_h:
    print("YES")
elif alarm_h > watch_h:
    print("NO")
else:
    if alarm_m < watch_m:
        print("YES")
    else:
        print("NO")
