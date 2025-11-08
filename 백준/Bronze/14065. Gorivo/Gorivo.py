import sys

n = float(sys.stdin.readline().strip())

result = 3.785411784 / (1.609344 * n) * 100

print(f"{result:.6f}")
