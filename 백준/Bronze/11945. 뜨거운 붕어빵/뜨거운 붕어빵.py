import sys

N, M = map(int, sys.stdin.readline().split())

boong_o_bbang = []
for _ in range(N):
    L = sys.stdin.readline().rstrip("\n")
    if len(L) != M:
        raise ValueError

    L_list = list(L)
    L_list.reverse()
    boong_o_bbang.append("".join(L_list))

print(*boong_o_bbang, sep="\n")
