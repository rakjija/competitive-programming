import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    print("PREMIADO" if n % 42 == 0 else "TENTE NOVAMENTE")
