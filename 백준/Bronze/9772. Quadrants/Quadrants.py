import sys

while True:
    x, y = map(float, sys.stdin.readline().split())

    if x > 0:
        if y > 0:
            print('Q1')
        elif y < 0:
            print('Q4')
        else:
            print('AXIS')
    elif x < 0:
        if y > 0:
            print('Q2')
        elif y < 0:
            print('Q3')
        else:
            print('AXIS')
    else:
        print('AXIS')
        if y == 0:
            break

