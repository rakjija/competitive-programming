def solution(code):
    ret = ''
    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            if mode == 0:
                mode = 1
            else:
                mode = 0
            continue
            
        if mode == 0:
            if i % 2 == 0:
                ret += code[i]
            continue
        else:
            if i % 2 != 0:
                ret += code[i]
            continue
    if len(ret) == 0:
        return 'EMPTY'
    return ret