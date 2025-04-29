import sys

N = int(sys.stdin.readline())
LABEL = "WelcomeToSMUPC"

print(LABEL[N % len(LABEL) - 1])
