import sys

d1: int = int(sys.stdin.readline().strip())
d2: int = int(sys.stdin.readline().strip())
PI: float = 3.141592

result: float = (d1 * 2) + (PI * d2 * 2)

print(f"{result}")
