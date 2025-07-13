import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().strip()
if N != len(S):
    raise ValueError(f"Expected length {N}, but got {len(S)}")

magic_count = 0
for i in range(N // 2):
    if S[i] != S[N - 1 - i]:
        magic_count += 1

print(magic_count)
