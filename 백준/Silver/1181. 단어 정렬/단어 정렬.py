import sys

N = int(sys.stdin.readline())

word_dict = {}
for _ in range(N):
    s = sys.stdin.readline().rstrip("\n")
    length = len(s)
    if length not in word_dict.keys():
        word_dict[length] = []
    if s not in word_dict[length]:
        word_dict[length].append(s)

result = []
for key in sorted(list(word_dict.keys())):
    word_dict[key].sort()
    result += word_dict[key]

print(*result, sep="\n")
