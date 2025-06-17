import sys

limit = int(sys.stdin.readline())
recorded = int(sys.stdin.readline())
over = recorded - limit

if over <= 0:
    print("Congratulations, you are within the speed limit!")
else:
    fine = 0
    if over >= 1 and over <= 20:
        fine = 100
    elif over >= 21 and over <= 30:
        fine = 270
    else:
        fine = 500
    print(f"You are speeding and your fine is ${fine}.")
