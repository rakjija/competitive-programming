def solution(a, b):
    A = int(str(a) + str(b))
    B = 2 * a * b
    if A >= B:
        return A
    return B