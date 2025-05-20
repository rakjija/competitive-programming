import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

card_dict = {}
for i in range(N):
    if cards[i] not in card_dict:
        card_dict[cards[i]] = 1
    else:
        card_dict[cards[i]] += 1

M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

result = []
for i in range(M):
    if targets[i] not in card_dict:
        result.append(0)
    else:
        result.append(card_dict[targets[i]])

print(*result)
