result = []
while True:
    S = input()
    if S == "0 0 0":
        break
    [A, B, C] = map(int, S.split())
    if (C**2 == A**2 + B**2) or (A**2 == B**2 + C**2) or (B**2 == C**2 + A**2):
        result.append("right")
    else:
        result.append("wrong")

print(*result, sep="\n")
