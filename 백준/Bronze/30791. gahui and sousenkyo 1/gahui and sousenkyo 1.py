import sys

votes = list(map(int, sys.stdin.readline().split()))

competition_rate = 0
rank_16th = votes[0]

for i in range(1, len(votes)):
    if rank_16th - votes[i] <= 1000:
        competition_rate += 1

print(competition_rate)
