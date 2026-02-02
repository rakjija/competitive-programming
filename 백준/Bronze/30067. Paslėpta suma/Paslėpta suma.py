import sys

num_list = []
for _ in range(10):
    num_list.append(int(sys.stdin.readline()))

for i, n in enumerate(num_list):
    if n == sum(num_list[:i] + num_list[i + 1 :]):
        print(n)
        break
