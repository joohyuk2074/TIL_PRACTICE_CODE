def solution(number):
    answer = recursive(0, 0, -1, number)

    return answer


def recursive(cnt, sum, index, number):
    if index >= len(number):
        return 0

    if cnt == 3:
        if sum == 0:
            return 1
        else:
            return 0

    return recursive(cnt + 1, sum + number[index], index + 1, number) + recursive(cnt, sum, index + 1, number)


def other_solution(number):
    from itertools import combinations
    cnt = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            cnt += 1
    return cnt
