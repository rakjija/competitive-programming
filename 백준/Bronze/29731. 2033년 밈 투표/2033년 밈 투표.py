import sys

memes = (
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop",
)

N = int(sys.stdin.readline())

hacked = False
for _ in range(N):
    S = sys.stdin.readline().rstrip("\n")
    if S not in memes:
        hacked = True
        break

print("Yes" if hacked else "No")
