assigned_student_list = []
for _ in range(28):
    assigned_student_id = int(input())
    assigned_student_list.append(assigned_student_id)

for i in range(1, 31):
    if i not in assigned_student_list:
        print(i)
