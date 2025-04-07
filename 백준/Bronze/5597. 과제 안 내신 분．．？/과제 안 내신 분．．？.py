student = [0] * 30
for i in range(28):
    student[int(input()) - 1] = 1
for i, v in enumerate(student):
    if v == 0:
        print(i + 1)
