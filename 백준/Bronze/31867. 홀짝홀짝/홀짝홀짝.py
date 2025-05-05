import sys

N = int(sys.stdin.readline())
K = sys.stdin.readline().rstrip()

count = 0
for i in range(N):
    if int(K[i]) % 2 == 0:
        count += 1
    else:
        count -= 1

if count > 0:
    print(0)
elif count < 0:
    print(1)
else:
    print(-1)
