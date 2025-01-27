sentences = []
while True:
    i = input()
    if i == ".":
        break
    sentences.append(i)

results = []
for sentence in sentences:
    stack = []
    flag = "yes"

    for char in sentence:
        if char in ["(", "["]:
            stack.append(char)
        elif char in [")", "]"]:
            if len(stack) == 0:
                flag = "no"
                break
            if char == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    flag = "no"
                    break
            if char == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    flag = "no"
                    break
    results.append(flag)

for result in results:
    print(result)
