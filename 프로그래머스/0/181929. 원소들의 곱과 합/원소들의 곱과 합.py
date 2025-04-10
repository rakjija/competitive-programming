def solution(num_list):
    A = 1
    for num in num_list:
        A *= num
    B = sum(num_list) ** 2
    return 1 if A < B else 0