import sys

width_list = [4, 2, 3, 3, 3, 3, 3, 3, 3, 3]

while True:
    N = sys.stdin.readline().rstrip("\n")
    if N == "0":
        break

    width = 2 + (len(N) - 1)
    for char in N:
        width += width_list[int(char)]

    print(width)
