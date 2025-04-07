X = {"A": 4, "B": 3, "C": 2, "D": 1}
Y = {"+": 0.3, "0": 0.0, "-": -0.3}

score = input()
if score == "F":
    print(0.0)
else:
    [score_x, score_y] = list(score)
    print(X[score_x] + Y[score_y])
