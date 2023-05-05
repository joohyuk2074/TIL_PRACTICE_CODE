def solution(a, d, included):
    answer = 0

    sum = a
    num_list = [a]
    for i in range(1, len(included)):
        sum += d
        num_list.append(sum)

    for i in range(len(included)):
        if included[i]:
            answer += num_list[i]

    return answer


def other_solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])
    return answer
