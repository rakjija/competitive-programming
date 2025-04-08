import sys

N = int(input())

stack = []
for _ in range(N):
    command = sys.stdin.readline().strip()

    if command.startswith("push"):
        stack.append(command.split()[-1])

    if command.startswith("pop"):
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    if command.startswith("size"):
        print(len(stack))

    if command.startswith("empty"):
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    if command.startswith("top"):
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
