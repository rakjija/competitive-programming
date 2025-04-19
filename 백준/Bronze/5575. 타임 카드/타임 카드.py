import sys

for _ in range(3):
    (
        on_h,
        on_m,
        on_s,
        off_h,
        off_m,
        off_s,
    ) = map(int, sys.stdin.readline().split())

    start = on_h * 60 * 60 + on_m * 60 + on_s
    end = off_h * 60 * 60 + off_m * 60 + off_s
    diff = end - start

    h = (diff // (60 * 60)) % 24
    m = (diff // 60) % 60
    s = diff % 60

    print(h, m, s)
