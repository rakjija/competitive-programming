import sys

scores = [13, 7, 5, 3, 3, 2]
cho = list(map(int, sys.stdin.readline().split()))
han = list(map(int, sys.stdin.readline().split()))

cho_sum = 0
han_sum = 1.5
for i, score in enumerate(scores):
    cho_sum += cho[i] * score
    han_sum += han[i] * score

print("cocjr0208" if cho_sum > han_sum else "ekwoo")
