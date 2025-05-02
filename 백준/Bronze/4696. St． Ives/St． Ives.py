import sys

while True:
    n = float(sys.stdin.readline())
    if n == 0:
        break

    print(f"{n**0 + n**1 + n**2 + n**3 + n**4:.2f}")
