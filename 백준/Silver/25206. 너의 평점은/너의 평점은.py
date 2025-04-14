import sys

grade_dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

total_grade = []
total_score = []
for _ in range(20):
    subjet, score, grade = sys.stdin.readline().split()
    if grade == "P":
        continue
    total_grade.append(float(score) * grade_dict[grade])
    total_score.append(float(score))

print(sum(total_grade) / sum(total_score))
