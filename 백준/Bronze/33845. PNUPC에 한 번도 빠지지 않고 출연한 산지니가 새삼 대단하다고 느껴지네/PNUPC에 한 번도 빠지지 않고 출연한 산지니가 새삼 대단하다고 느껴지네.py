import sys

S: str = sys.stdin.readline().strip()
T: str = sys.stdin.readline().strip()

remove_duplicate_chars: set[str] = set(S)

result: str = "".join([char for char in T if char not in remove_duplicate_chars])

print(result)
