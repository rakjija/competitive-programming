S = input()
checker = [-1] * 26
for i, char in enumerate(S):
    if checker[ord(char) - ord("a")] == -1:
        checker[ord(char) - ord("a")] = i
print(" ".join(map(str, checker)))
