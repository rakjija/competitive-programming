import sys

bigdata = {"l": 0, "k": 0, "p": 0}
result = "GLOBAL"
for _ in range(3):
    S = sys.stdin.readline().rstrip()
    try:
        bigdata[S[0]] += 1
    except Exception:
        continue

if 0 in set(bigdata.values()):
    result = "PONIX"

print(result)
