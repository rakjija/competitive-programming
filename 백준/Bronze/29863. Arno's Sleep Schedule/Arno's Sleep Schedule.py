import sys

sleep_time = int(sys.stdin.readline().rstrip("\n"))
wake_time = int(sys.stdin.readline().rstrip("\n"))

if sleep_time >= 20:
    print((24 - sleep_time) + wake_time)
elif sleep_time <= 3:
    print(wake_time - sleep_time)
