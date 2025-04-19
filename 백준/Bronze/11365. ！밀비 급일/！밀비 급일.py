import sys

while True:
    S = sys.stdin.readline().rstrip("\n")
    if S == "END":
        break

    S_list = list(S)
    S_list.reverse()

    print("".join(S_list))
