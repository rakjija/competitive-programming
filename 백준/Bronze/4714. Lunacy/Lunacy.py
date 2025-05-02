import sys

while True:
    n = float(sys.stdin.readline())
    if n < 0:
        break

    print(f"Objects weighing {n:.2f} on Earth will weigh {n * 0.167:.2f} on the moon.")
