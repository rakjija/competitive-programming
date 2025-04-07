while True:
    try:
        [A, B] = map(int, input().split(" "))
        print(A + B)
    except Exception:
        break

"""
문제에는 정확히 명시되어 있지 않지만..
확인해야할 것은
1. 결과값 출력은 입력 후 바로 이루어져야 함
2. 이 프로그램의 종료는 입력값이 잘못되어 예외가 발생했을 경우임
"""
