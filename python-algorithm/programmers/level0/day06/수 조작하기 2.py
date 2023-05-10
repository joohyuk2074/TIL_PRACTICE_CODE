def solution(numLog):
    answer = ''

    my_dict = {
        1: 'w',
        -1: 's',
        10: 'd',
        -10: 'a'
    }
    for i in range(len(numLog) - 1):
        num = numLog[i + 1] - numLog[i]
        answer += my_dict[num]

    return answer


def other_solution(log):
    res = ''
    joystick = dict(zip([1, -1, 10, -10], ['w', 's', 'd', 'a']))
    for i in range(1, len(log)):
        res += joystick[log[i] - log[i - 1]]
    return res


arr = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]
print(solution(arr))
