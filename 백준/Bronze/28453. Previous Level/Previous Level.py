import sys

n = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

result: list[str] = []
for i in range(n):
    lv = m_list[i]

    sec = None
    if lv < 250:
        sec = 4
    elif 250 <= lv < 275:
        sec = 3
    elif 275 <= lv < 300:
        sec = 2
    elif lv == 300:
        sec = 1

    result.append(str(sec))


print(" ".join(result))
