import sys

T = int(sys.stdin.readline().rstrip("\n"))

for _ in range(T):
    input, output = sys.stdin.readline().split()
    print("OK" if input == output else "ERROR")
