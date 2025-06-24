import sys

cards = {
    "STRAWBERRY": 0,
    "BANANA": 0,
    "LIME": 0,
    "PLUM": 0,
}

N = int(sys.stdin.readline())
for _ in range(N):
    S, X = sys.stdin.readline().split()
    cards[S] += int(X)

print("YES" if 5 in cards.values() else "NO")
