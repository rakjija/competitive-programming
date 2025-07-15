import sys

N, M, K = map(int, sys.stdin.readline().split())

s_list = []
p_list = []
for _ in range(N):
    s, p = sys.stdin.readline().split()
    s_list.append(s)
    p_list.append(int(p))

t_list = []
for _ in range(K):
    t_list.append(sys.stdin.readline().strip())

base_score = 0
for t in t_list:
    index = s_list.index(t)
    s_list.remove(t)
    base_score += p_list.pop(index)

p_list.sort()
min_score = base_score + sum(p_list[: M - K])
max_score = base_score + sum(p_list[len(p_list) - (M - K) :])

print(min_score, max_score)
