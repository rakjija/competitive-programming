import sys
from typing import cast

s = sys.stdin.readline().strip()

c_dict = cast(dict[str, int], {})

for c in s:
    c_lower = c.lower()
    if c_lower not in c_dict:
        c_dict[c_lower] = 0
    c_dict[c_lower] += 1

max_value = max(c_dict.values())
if list(c_dict.values()).count(max_value) > 1:
    print("?")
else:
    for k, v in c_dict.items():
        if v == max_value:
            print(k.upper())
            break
