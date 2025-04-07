import sys

T = int(input())

result = []
for i in range(T):
    [A, B] = map(int, sys.stdin.readline().rstrip().split())
    result.append(A + B)
print(*result, sep="\n")


"""
input() 보다는 
sys.stdin.readline()이 더 빠르다
단, 이 경우 개행문자까지 입력을 받는다.
따라서, rstrip()을 사용하여 마지막에 입력된 개행문자도 제거하는 것이 좋다.
"""
