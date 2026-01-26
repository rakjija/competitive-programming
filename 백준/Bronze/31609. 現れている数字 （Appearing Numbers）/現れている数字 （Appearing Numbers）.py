import sys

n = int(sys.stdin.readline())
a_list = sys.stdin.readline().split()

print("\n".join(sorted(list(set(a_list)))))
