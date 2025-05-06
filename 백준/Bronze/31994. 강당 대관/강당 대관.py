import sys

main = ["", "0"]
for _ in range(7):
    S = sys.stdin.readline().split()
    if int(main[1]) < int(S[1]):
        main = S

print(main[0])
