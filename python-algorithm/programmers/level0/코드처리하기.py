def solution(code):
    answer = ''

    mode = 0
    code_length = len(code)
    for i in range(code_length):
        if mode == 0:
            if code[i] != '1':
                if i % 2 == 0:
                    answer += code[i]
            else:
                mode = 1
        else:
            if code[i] != '1':
                if i % 2 == 1:
                    answer += code[i]
            else:
                mode = 0

    if answer == '':
        return "EMPTY"

    return answer


def other_solution(code):
    answer = ''

    mode = 0
    for i in range(len(code)):
        if code[i] == ' 1':
            mode ^= 1
        else:
            if i % 2 == mode:
                answer += code[i]

    return answer if answer else 'EMPTY'


print(solution("abc1abc1abc"))
