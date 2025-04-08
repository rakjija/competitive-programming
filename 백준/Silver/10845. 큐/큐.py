import sys

N = int(sys.stdin.readline().strip())

queue = []
for _ in range(N):
    command = sys.stdin.readline().strip()

    if command.startswith("push"):
        queue.append(command.split()[-1])

    if command == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue = queue[1:]

    if command == "size":
        print(len(queue))

    if command == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    if command == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    if command == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
