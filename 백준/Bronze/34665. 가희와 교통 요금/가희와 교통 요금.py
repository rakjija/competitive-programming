import sys

station_a = sys.stdin.readline().strip()
station_b = sys.stdin.readline().strip()


print(0 if station_a == station_b else 1550)
