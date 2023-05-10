from functools import reduce


def solution(num_list):
    answer = 0

    if len(num_list) >= 11:
        answer = sum(num_list)
    elif len(num_list) <= 10:
        answer = reduce(lambda x, y: x * y, num_list)

    return answer


def other_solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(list(map(str, num_list))))
    else:
        return eval('*'.join(list(map(str, num_list))))