import sys

n = int(sys.stdin.readline())

winner: str = ""
for _ in range(n):
    u: str = sys.stdin.readline().strip()

    if winner == "" and (u == "yonsei" or u == "korea"):
        winner = u

print("Yonsei Won!" if winner == "yonsei" else "Yonsei Lost...")
