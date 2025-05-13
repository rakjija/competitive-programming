import sys

N = int(sys.stdin.readline())

if N >= -(2**15) and N <= 2**15 - 1:
    print("short")
elif N >= -(2**31) and N <= 2**31 - 1:
    print("int")
elif N >= -(2**63) and N <= 2**63 - 1:
    print("long long")
