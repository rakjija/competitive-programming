import sys

oct_dict = {
    "-": 0,
    "\\": 1,
    "(": 2,
    "@": 3,
    "?": 4,
    ">": 5,
    "&": 6,
    "%": 7,
    "/": -1,
}

while True:
    S = sys.stdin.readline().rstrip("\n")
    if S == "#":
        break

    total = 0
    for i in range(len(S)):
        index = len(S) - i - 1
        total += oct_dict[S[i]] * (8**index)

    print(total)
