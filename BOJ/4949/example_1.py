while True:
    s = input()
    if s == ".":
        break

    stack = []
    balanced = True

    for i in range(len(s)):
        if s[i] == "(" or s[i] == "[":
            stack.append(s[i])

        # 1
        if s[i] == ")":
            # 4
            if len(stack) == 0:
                balanced = False
                break

            # 3
            last = stack.pop(-1)
            if last != "(":
                balanced = False
                break

        # 2
        if s[i] == "]":
            # 6
            if len(stack) == 0:
                balanced = False
                break

            # 5
            last = stack.pop(-1)
            if last != "[":
                balanced = False
                break

    if len(stack) != 0:
        balanced = False

    if balanced:
        print("yes")
    else:
        print("no")
