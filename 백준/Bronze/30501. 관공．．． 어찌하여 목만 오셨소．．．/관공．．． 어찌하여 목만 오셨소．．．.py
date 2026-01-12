import sys
from typing import cast

n = int(sys.stdin.readline())

criminal = ""
for _ in range(n):
    name = cast(str, sys.stdin.readline().strip())

    if "S" in name:
        criminal = name

print(criminal)
