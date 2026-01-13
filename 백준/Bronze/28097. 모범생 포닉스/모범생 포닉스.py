import sys

n = int(sys.stdin.readline())
t_list = list(map(int, sys.stdin.readline().split()))

time = 0
for i in range(n):
    tn = t_list[i]
    time += tn
    if i != n - 1:
        time += 8  # 8H breaking time between plans

print(int(time / 24), time % 24)
