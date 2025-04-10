def solution(num_list):
    even = ''
    odd = ''
    for num in num_list:
        if num % 2 == 0:
            even += str(num)
        else:
            odd += str(num)
    if even == '':
        even = 0
    if odd == '':
        odd = 0
    return int(even) + int(odd)