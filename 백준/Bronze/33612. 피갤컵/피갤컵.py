import sys

N = int(sys.stdin.readline().strip())

added_month = 1 + (7 * N)
year = 2024 + (added_month - 1) // 12
month = (added_month - 1) % 12 + 1

print(year, month)
