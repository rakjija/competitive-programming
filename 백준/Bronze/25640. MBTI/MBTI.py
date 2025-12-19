import sys

joho_type = sys.stdin.readline().strip()
n = int(sys.stdin.readline())

same_count = 0
for _ in range(n):
    friend_type = sys.stdin.readline().strip()
    if joho_type == friend_type:
        same_count += 1

print(same_count)
