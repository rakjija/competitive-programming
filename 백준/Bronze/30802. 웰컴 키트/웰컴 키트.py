import math

N = int(input())
sizes = map(int, input().split())
[T, P] = map(int, input().split())
T_pack = 0
for size in sizes:
    T_pack += math.ceil(size / T)
print(T_pack)
print(N // P, N % P)
