import math
import sys

for line in sys.stdin:
    line = line.strip()
    if line == "0 0 0 0":
        break
    values = list(map(int, line.split()))

    target_index = values.index(0)
    if target_index == 3:
        values[target_index] = math.prod(values[:-1])
    else:
        values[target_index] = values[-1] // math.prod(
            [v for i, v in enumerate(values[0:-1]) if i != target_index]
        )

    print(*values)
