import sys

w = float(sys.stdin.readline())
h = float(sys.stdin.readline())

bmi = w / (h * h)

if bmi > 25:
    print("Overweight")
elif bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 25.0:
    print("Normal weight")
