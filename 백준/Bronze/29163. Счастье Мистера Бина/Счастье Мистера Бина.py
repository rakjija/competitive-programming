import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
if n != len(a):
    raise ValueError

emotion = 0
for i in range(n):
    if a[i] % 2 == 0:
        emotion += 1
    else:
        emotion -= 1

print("Happy" if emotion > 0 else "Sad")
