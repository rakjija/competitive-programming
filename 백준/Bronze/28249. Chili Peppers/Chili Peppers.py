import sys

shu_dict = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000,
}

N = int(sys.stdin.readline())

T = 0
for _ in range(N):
    pepper = sys.stdin.readline().rstrip("\n")
    T += shu_dict[pepper]

print(T)
